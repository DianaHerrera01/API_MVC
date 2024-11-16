from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from modulos.notas.models import Nota, TipoNota, ProductoNota
from modulos.producto.models import Producto, Categoria
from modulos.factura.models import Factura, DetalleFactura
from modulos.cliente.models import Cliente, TipoDocumento

class TipoNotaTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Crear una instancia de TipoNota de ejemplo
        self.tipo_nota = TipoNota.objects.create(nom_nota="Descuento")

    def test_create_tipo_nota(self):
        url = reverse('tipo-nota-list-create')
        data = {
            "nom_nota": "Devolución"
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_tipo_nota(self):
        url = reverse('tipo-nota-retrieve-update-destroy', args=[self.tipo_nota.id_tipo_nota])
        data = {
            "nom_nota": "Cambio de Producto"
        }
        response = self.client.put(url, data, format='json')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_tipo_nota(self):
        url = reverse('tipo-nota-retrieve-update-destroy', args=[self.tipo_nota.id_tipo_nota])
        response = self.client.get(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom_nota'], self.tipo_nota.nom_nota)

    def test_delete_tipo_nota(self):
        url = reverse('tipo-nota-retrieve-update-destroy', args=[self.tipo_nota.id_tipo_nota])
        response = self.client.delete(url)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class NotaTests(TestCase):
    def setUp(self):
        # Crear categoría y producto de prueba
        self.categoria = Categoria.objects.create(nom_categoria="Electrónica")
        self.producto = Producto.objects.create(
            nombre_producto="Smartphone",
            cantidad=50,
            descripcion="Un smartphone de prueba",
            categoria=self.categoria,
            preciounidadcompra=800.00,
            preciounidadventa=1000.00
        )

        self.tipo_documento = TipoDocumento.objects.create(nom_tipo_doc="Factura")
        # Configuración de datos de prueba para las entidades relacionadas
        self.cliente = Cliente.objects.create(
            nombre_cliente="Juan",
            apellidos_cliente="Pérez",
            correo="juan.perez@test.com",
            id_tipo_docum=self.tipo_documento,
            documento_cli="1234567890",
            telefono="3201234567"
        )
        # Crear factura
        self.factura = Factura.objects.create(
            cliente=self.cliente,
            tipo_documento=self.tipo_documento,
            fecha_emision="2024-11-15"
        )

        # Crear un detalle de la factura
        detalles = DetalleFactura.objects.create(
            factura=self.factura, 
            producto=self.producto, 
            cantidad=2
        )

        # Crear TipoNota de prueba
        self.tipo_nota = TipoNota.objects.create(nom_nota="Nota de Crédito")

    def test_create_nota(self):
        url = reverse('nota-list-create')
        data = {
            "factura": self.factura.id_factura,
            "tipo_nota": self.tipo_nota.id_tipo_nota,
            "motivo": "Producto defectuoso",
            "valor": 0.00,
            "productos": [
                {
                    "producto": self.producto.id_producto,
                    "cantidad": 2
                }
            ]
        }
        response = self.client.post(url, data, content_type="application/json")
        
        # Imprimir detalles de la respuesta
        print(response.status_code)
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Nota.objects.count(), 1)
        self.assertEqual(TipoNota.objects.count(), 1)

    def test_update_nota(self):
        # Crear una nota inicial
        nota = Nota.objects.create(
            factura=self.factura,
            tipo_nota=self.tipo_nota,
            motivo="Producto en mal estado",
            valor=0.00,
        )
        ProductoNota.objects.create(
            nota=nota,
            producto=self.producto,
            cantidad=1
        )

        # Endpoint para actualizar la nota
        url = reverse('nota-retrieve-update-destroy', args=[nota.id_nota])
        data = {
            "factura": self.factura.id_factura,
            "tipo_nota": self.tipo_nota.id_tipo_nota,
            "motivo": "Motivo actualizado",
            "valor": 1500.00,
            "productos": [
                {
                    "producto": self.producto.id_producto,
                    "cantidad": 3
                }
            ]
        }
        response = self.client.put(url, data, content_type="application/json")
        
        # Imprimir detalles de la respuesta
        print(response.status_code)
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_nota(self):
        # Crear una nota de prueba
        nota = Nota.objects.create(
            factura=self.factura,
            tipo_nota=self.tipo_nota,
            motivo="Producto defectuoso",
            valor=0.00,
        )
        ProductoNota.objects.create(
            nota=nota,
            producto=self.producto,
            cantidad=1
        )

        url = reverse('nota-retrieve-update-destroy', args=[nota.id_nota])
        response = self.client.get(url)
        print(response.status_code)
        print(response.data)
        
        # Comprobar que la respuesta es correcta
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_nota(self):
        # Crear una nota inicial para eliminar
        nota = Nota.objects.create(
            factura=self.factura,
            tipo_nota=self.tipo_nota,
            motivo="Producto defectuoso",
            valor=0.00,
        )
        ProductoNota.objects.create(
            nota=nota,
            producto=self.producto,
            cantidad=1
        )

        url = reverse('nota-retrieve-update-destroy', args=[nota.id_nota])
        response = self.client.delete(url)
        
        # Imprimir detalles de la respuesta
        print(response.status_code)
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Nota.objects.count(), 0)



