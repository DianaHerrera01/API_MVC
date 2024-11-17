from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from django.contrib.auth.models import User

class TestRegistroView(TestCase): 
    
    def setUp(self):
        # Crear un usuario para pruebas de autenticación y actualización
        self.user = User.objects.create_user(
            username="usuario_prueba",
            email="prueba@example.com",
            password="Password123!"
        )
    
    def test_registro_usuario(self):
        # Test para registrar un usuario nuevo
        url = reverse('registro')
        data = {
            "username": "nuevo_usuario",
            "email": "nuevo@example.com",
            "password": "Password123!",
            "password2": "Password123!",
            "first_name": "Nuevo",
            "last_name": "Usuario"
        }
        response = self.client.post(url, data, content_type='application/json')  # Usamos content_type 'application/json'
        print(response.status_code)
        print(response.data)  # Imprimir el contenido de la respuesta
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['mensaje'], "Usuario registrado correctamente.")

    def test_registro_usuario_existente(self):
        # Test para evitar registro con un nombre de usuario ya existente
        url = reverse('registro')
        data = {
            "username": "usuario_prueba",
            "email": "nuevo_email@example.com",
            "password": "Password123!",
            "password2": "Password123!"
        }
        response = self.client.post(url, data, content_type='application/json')  # Usamos content_type 'application/json'
        print(response.status_code)
        print(response.data)  # Imprimir el contenido de la respuesta
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('unique', response.data['username'][0].code)  

    def test_actualizar_usuario(self):
        url = reverse('usuario_detalle', kwargs={'pk': self.user.id})  # Cambiado a 'registro_detalle'
        data = {
            "username": "usuario_actualizado",
            "email": "actualizado@example.com",
            "password": "NewPassword123!",
            "password2": "NewPassword123!",
            "first_name": "Usuario",
            "last_name": "Actualizado"
        }
        response = self.client.put(url, data, content_type='application/json')
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_eliminar_usuario(self):
        url = reverse('usuario_detalle', kwargs={'pk': self.user.id})  # Cambiado a 'registro_detalle'
        response = self.client.delete(url)
        print(response.status_code)
        
        # Aseguramos que no intentamos hacer un json() si no hay contenido
        if response.status_code == status.HTTP_204_NO_CONTENT:
            print("Respuesta sin contenido")  # Imprimir si la respuesta está vacía
        else:
            print(response.json())  # Si hay contenido, mostrarlo
        
        # Verificamos que el estado sea 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
   
    def test_listar_usuarios(self):
        url = reverse('registro')
        response = self.client.get(url)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)  # Salida JSON como lista
        self.assertGreater(len(response.json()), 0)  # Asegurar que hay usuarios



class TestLoginView(TestCase):  # nombre de la clase
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('token_obtain_pair')
        self.user = User.objects.create_user(username="usuario_prueba", password="Password123!")
        self.login_data = {
            "username": "usuario_prueba",
            "password": "Password123!"
        }

    def test_user_login_successful(self):
        response = self.client.post(self.url, self.login_data, format='json')
        print(response.status_code)
        print(response.data)  # Imprimir el contenido de la respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensaje', response.data)
        self.assertEqual(response.data['mensaje'], "Autenticación satisfactoria.")
        self.assertIn('access', response.data)  # Verificar que el token esté presente
