from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from modulos.producto.models import Producto, Categoria
from modulos.proveedor.models import Proveedor
from modulos.Devolucion.models import Devolucion

class DevolucionTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear proveedor, categoría y producto
        self.proveedor = Proveedor.objects.create(
            nombre_proveedor="Proveedor Test",
            apellidos_proveedor="Apellidos Test",
            correo="proveedor@test.com",
            direccion="Direccion Test",
            telefono="1234567890"
        )
        
        self.categoria = Categoria.objects.create(
            nom_categoria="Electrónica"
        )
        
        self.producto = Producto.objects.create(
            nombre_producto="Laptop Test",
            cantidad=20,
            descripcion="Laptop de prueba",
            categoria=self.categoria,
            proveedor=self.proveedor,
            preciounidadcompra=1500.00,
            preciounidadventa=1800.00
        )
        
        self.devolucion = Devolucion.objects.create(
            producto=self.producto,
            proveedor=self.proveedor,
            cantidad=5,
            motivo="Producto defectuoso",
            fecha_devolucion="2024-11-15"
        )

    def test_create_devolucion(self):
        url = reverse('devolucion-list-create')
        data = {
            "producto": self.producto.id_producto,
            "proveedor": self.proveedor.id_proveedor,
            "cantidad": 3,
            "motivo": "Error en el pedido",
            "fecha_devolucion": "2024-11-15"
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['cantidad'], 3)

    def test_update_devolucion(self):
        url = reverse('devolucion-detail', args=[self.devolucion.id_devolucion])
        data = {
            "producto": self.producto.id_producto,
            "proveedor": self.proveedor.id_proveedor,
            "cantidad": 7,
            "motivo": "Cantidad incorrecta",
            "fecha_devolucion": "2024-11-15"
        }
        response = self.client.put(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cantidad'], 7)

    def test_retrieve_devolucion(self):
        url = reverse('devolucion-detail', args=[self.devolucion.id_devolucion])
        response = self.client.get(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cantidad'], self.devolucion.cantidad)

    def test_delete_devolucion(self):
        url = reverse('devolucion-detail', args=[self.devolucion.id_devolucion])
        response = self.client.delete(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    