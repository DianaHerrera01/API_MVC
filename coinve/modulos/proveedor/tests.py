from django.test import TestCase 
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Proveedor, ProductoServicio

class ProveedorTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear un producto/servicio de ejemplo
        self.producto = ProductoServicio.objects.create(nom_producto_serv="ProductoServTest")
        
        # Crear un proveedor de ejemplo
        self.proveedor = Proveedor.objects.create(
            nombre_proveedor="Proveedor Test",
            apellidos_proveedor="Apellidos Test",
            correo="proveedor@test.com",
            direccion="Direccion Test",
            telefono="1234567890"
        )
        self.proveedor.productos_servicios.add(self.producto)
    
    def test_create_proveedor(self):
        url = reverse('proveedor-list-create')
        data = {
            "nombre_proveedor": "Nuevo Proveedor",
            "apellidos_proveedor": "Nuevos Apellidos",
            "correo": "nuevo@proveedor.com",
            "direccion": "Nueva Direccion",
            "telefono": "0987654321",
            "productos_servicios": [self.producto.id_producto_servicio]
        }
        response = self.client.post(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_proveedor(self):
        url = reverse('proveedor-detail', args=[self.proveedor.id_proveedor])
        data = {
            "nombre_proveedor": "Proveedor Actualizado",
            "apellidos_proveedor": "Apellidos Actualizados",
            "correo": "actualizado@proveedor.com",
            "direccion": "Direccion Actualizada",
            "telefono": "1122334455",
            "productos_servicios": [self.producto.id_producto_servicio]
        }
        response = self.client.put(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_retrieve_proveedor(self):
        url = reverse('proveedor-detail', args=[self.proveedor.id_proveedor])
        response = self.client.get(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_proveedor(self):
        url = reverse('proveedor-detail', args=[self.proveedor.id_proveedor])
        response = self.client.delete(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductoServicioTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear un producto/servicio de ejemplo
        self.producto = ProductoServicio.objects.create(nom_producto_serv="ProductoServ Test")

    def test_create_producto_servicio(self):
        url = reverse('producto-servicio-list-create')
        data = {
            "nom_producto_serv": "Nuevo Producto Servicio"
        }
        response = self.client.post(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_producto_servicio(self):
        url = reverse('producto-servicio-detail', args=[self.producto.id_producto_servicio])
        response = self.client.get(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('nom_producto_serv'), self.producto.nom_producto_serv)

    def test_update_producto_servicio(self):
        url = reverse('producto-servicio-detail', args=[self.producto.id_producto_servicio])
        data = {
            "nom_producto_serv": "Producto Servicio Actualizado"
        }
        response = self.client.put(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_producto_servicio(self):
        url = reverse('producto-servicio-detail', args=[self.producto.id_producto_servicio])
        response = self.client.delete(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
