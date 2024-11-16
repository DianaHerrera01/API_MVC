from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import TipoDocumento, Cliente

class TipoDocumentoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Crear un TipoDocumento de ejemplo
        self.tipo_documento = TipoDocumento.objects.create(nom_tipo_doc="Cédula de Ciudadanía")

    def test_create_tipo_documento(self):
        url = reverse('tipo-documento-list-create')
        data = {
            "nom_tipo_doc": "Pasaporte"
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_tipo_documento(self):
        url = reverse('tipo-documento-detail', args=[self.tipo_documento.id_tipo_docum])
        response = self.client.get(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('nom_tipo_doc'), self.tipo_documento.nom_tipo_doc)

    def test_update_tipo_documento(self):
        url = reverse('tipo-documento-detail', args=[self.tipo_documento.id_tipo_docum])
        data = {
            "nom_tipo_doc": "Tarjeta de Identidad"
        }
        response = self.client.put(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_tipo_documento(self):
        url = reverse('tipo-documento-detail', args=[self.tipo_documento.id_tipo_docum])
        response = self.client.delete(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ClienteTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Crear un TipoDocumento de ejemplo
        self.tipo_documento = TipoDocumento.objects.create(nom_tipo_doc="Cédula de Ciudadanía")
        # Crear un Cliente de ejemplo
        self.cliente = Cliente.objects.create(
            nombre_cliente="Juan",
            apellidos_cliente="Pérez",
            correo="juan.perez@test.com",
            id_tipo_docum=self.tipo_documento,
            documento_cli="1234567890",
            telefono="3201234567"
        )

    def test_create_cliente(self):
        url = reverse('cliente-list-create')
        data = {
            "nombre_cliente": "María",
            "apellidos_cliente": "Gómez",
            "correo": "maria.gomez@test.com",
            "tipo_documento": self.tipo_documento.id_tipo_docum,
            "documento_cli": "0987654321",
            "telefono": "3109876543"
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_cliente(self):
        url = reverse('cliente-detail', args=[self.cliente.id_cliente])
        response = self.client.get(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('nombre_cliente'), self.cliente.nombre_cliente)

    def test_update_cliente(self):
        url = reverse('cliente-detail', args=[self.cliente.id_cliente])
        data = {
            "nombre_cliente": "Carlos",
            "apellidos_cliente": "Martínez",
            "correo": "carlos.martinez@test.com",
            "tipo_documento": self.tipo_documento.id_tipo_docum,
            "documento_cli": "1234567890",
            "telefono": "3001234567"
        }
        response = self.client.put(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_cliente(self):
        url = reverse('cliente-detail', args=[self.cliente.id_cliente])
        response = self.client.delete(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
