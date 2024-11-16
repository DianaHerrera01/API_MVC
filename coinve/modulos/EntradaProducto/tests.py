from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from modulos.producto.models import Producto, Categoria
from modulos.proveedor.models import Proveedor
from modulos.Pedido.models import Pedido
from .models import Entrada

class EntradaTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Crear proveedor, producto, categoría y pedido
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

        # Crear una entrada inicial
        self.entrada = Entrada.objects.create(
            pedido=self.pedido,
            producto=self.producto,
            categoria=self.categoria,
            proveedor=self.proveedor,
            cantidad=5,
            fecha="2024-11-14"
        )

    def test_create_entrada(self):
        url = reverse('entrada-list-create')
        data = {
            "pedido": self.pedido.id_orden_pedido,
            "producto": self.producto.id_producto,
            "categoria": self.categoria.categoriaID,
            "proveedor": self.proveedor.id_proveedor,
            "cantidad": 10,
            "fecha": "2024-11-14"
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_entrada(self):
        url = reverse('entrada-detail', args=[self.entrada.id_entrada])
        data = {
            "pedido": self.pedido.id_orden_pedido,
            "producto": self.producto.id_producto,
            "categoria": self.categoria.categoriaID,
            "proveedor": self.proveedor.id_proveedor,
            "cantidad": 15,
            "fecha": "2024-11-15"
        }
        response = self.client.put(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_entrada(self):
        url = reverse('entrada-detail', args=[self.entrada.id_entrada])
        response = self.client.get(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_entrada(self):
        url = reverse('entrada-detail', args=[self.entrada.id_entrada])
        response = self.client.delete(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
