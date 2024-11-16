from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from modulos.producto.models import Producto, Categoria
from modulos.proveedor.models import Proveedor

class CategoriaTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear una categoría de ejemplo
        self.categoria = Categoria.objects.create(nom_categoria="Electrónica")

    def test_create_categoria(self):
        url = reverse('categoria-list-create')
        data = {
            "nom_categoria": "Computadoras"
        }
        response = self.client.post(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_categoria(self):
        url = reverse('categoria-detail', args=[self.categoria.categoriaID])
        data = {
            "nom_categoria": "Tecnología Avanzada"
        }
        response = self.client.put(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_categoria(self):
        url = reverse('categoria-detail', args=[self.categoria.categoriaID])
        response = self.client.get(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom_categoria'], self.categoria.nom_categoria)

    def test_delete_categoria(self):
        url = reverse('categoria-detail', args=[self.categoria.categoriaID])
        response = self.client.delete(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear una categoría de ejemplo
        self.categoria = Categoria.objects.create(nom_categoria="Electrónica")
        
        # Crear un proveedor de ejemplo
        self.proveedor = Proveedor.objects.create(
            nombre_proveedor="Proveedor Test",
            apellidos_proveedor="Apellidos Test",
            correo="proveedor@test.com",
            direccion="Direccion Test",
            telefono="1234567890"
        )
        
        # Crear un producto de ejemplo
        self.producto = Producto.objects.create(
            nombre_producto="Laptop Test",
            cantidad=10,
            categoria=self.categoria,
            descripcion="Laptop de prueba",
            proveedor=self.proveedor,
            preciounidadcompra=1000.00,
            preciounidadventa=1200.00
        )

    def test_create_producto(self):
        url = reverse('producto-list-create')
        data = {
            "nombre_producto": "Smartphone Test",
            "cantidad": 50,
            "categoria": self.categoria.categoriaID,
            "descripcion": "Smartphone de prueba",
            "proveedor": self.proveedor.id_proveedor,
            "preciounidadcompra": 200.00,
            "preciounidadventa": 250.00
        }
        response = self.client.post(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_producto(self):
        url = reverse('producto-detail', args=[self.producto.id_producto])
        data = {
            "nombre_producto": "Laptop Actualizada",
            "cantidad": 5,
            "categoria": self.categoria.categoriaID,
            "descripcion": "Laptop actualizada",
            "proveedor": self.proveedor.id_proveedor,
            "preciounidadcompra": 1100.00,
            "preciounidadventa": 1300.00
        }
        response = self.client.put(url, data, format='json')
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_producto(self):
        url = reverse('producto-detail', args=[self.producto.id_producto])
        response = self.client.get(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_producto'], self.producto.nombre_producto)

    def test_delete_producto(self):
        url = reverse('producto-detail', args=[self.producto.id_producto])
        response = self.client.delete(url)
        # Imprimir el código de estado y la respuesta en JSON
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
