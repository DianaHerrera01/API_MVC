from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from modulos.producto.models import Producto, Categoria
from modulos.proveedor.models import Proveedor
from modulos.Pedido.models import Pedido

class PedidoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear proveedor, producto y categoría
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
            cantidad=10,
            descripcion="Laptop de prueba",
            categoria=self.categoria,
            proveedor=self.proveedor,
            preciounidadcompra=1000.00,
            preciounidadventa=1200.00
        )
        
        self.pedido = Pedido.objects.create(
            proveedor=self.proveedor,
            producto=self.producto,
            cantidad=5,
            estado='Pendiente'
        )

    def test_create_pedido(self):
        url = reverse('pedido-list-create')
        data = {
            "proveedor": self.proveedor.id_proveedor,
            "producto": self.producto.id_producto,
            "cantidad": 10,
            "estado": "Pendiente"
        }
        response = self.client.post(url, data, format='json')
        # Imprimir código de estado y contenido de la respuesta
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_pedido(self):
        url = reverse('pedido-detail', args=[self.pedido.id_orden_pedido])
        data = {
            "proveedor": self.proveedor.id_proveedor,
            "producto": self.producto.id_producto,
            "cantidad": 20,
            "estado": "En Proceso"
        }
        response = self.client.put(url, data, format='json')
        # Imprimir código de estado y contenido de la respuesta
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_pedido(self):
        url = reverse('pedido-detail', args=[self.pedido.id_orden_pedido])
        response = self.client.get(url)
        # Imprimir código de estado y contenido de la respuesta
        print("Test Retrieve Pedido")
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pedido(self):
        url = reverse('pedido-detail', args=[self.pedido.id_orden_pedido])
        response = self.client.delete(url)
        # Imprimir código de estado y contenido de la respuesta
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
