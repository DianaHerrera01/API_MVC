import json
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from .models import Factura, DetalleFactura
from modulos.cliente.models import TipoDocumento, Cliente
from modulos.producto.models import Producto, Categoria


class FacturaTests(TestCase):
    def setUp(self):
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
        
        self.categoria = Categoria.objects.create(
            nom_categoria="Electrónica"
        )
        
        self.producto = Producto.objects.create(
            nombre_producto="Laptop Test",
            cantidad=10,
            descripcion="Laptop de prueba",
            categoria=self.categoria,
            preciounidadcompra=1000.00,
            preciounidadventa=1200.00
        )

    def test_create_factura(self):
        url = reverse('factura-list-create')
        data = {
            "cliente": self.cliente.id_cliente,
            "tipo_documento": self.tipo_documento.id_tipo_docum,
            "fecha_emision": "2024-11-15",
            "detalles": [
                {
                    "producto": self.producto.id_producto,
                    "cantidad": 2,
                }
            ]
        }
        response = self.client.post(
            url,
            data=json.dumps(data),  # Convertimos a JSON
            content_type='application/json'  # Especificamos el encabezado correcto
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_factura(self):
        # Creamos una factura existente
        factura = Factura.objects.create(
            cliente=self.cliente,
            tipo_documento=self.tipo_documento,
            fecha_emision="2024-11-15",
            precio_total_venta=300000
        )
        DetalleFactura.objects.create(
            factura=factura,
            producto=self.producto,
            cantidad=2,
            precio_total_venta=300000
        )

        # Datos para actualizar la factura
        data = {
            "cliente": self.cliente.id_cliente,
            "tipo_documento": self.tipo_documento.id_tipo_docum,
            "fecha_emision": "2024-11-16",
            "detalles": [
                {
                    "producto": self.producto.id_producto,
                    "cantidad": 3  # Actualizamos la cantidad
                }
            ]
        }
        url = reverse('factura-detail', kwargs={'pk': factura.id_factura})
        response = self.client.put(
            url,
            data=json.dumps(data),  # Convertimos a JSON
            content_type='application/json'  # Especificamos el encabezado correcto
        )

        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificamos que la factura se haya actualizado correctamente
        factura.refresh_from_db()
        from datetime import date
        self.assertEqual(factura.fecha_emision, date(2024, 11, 16))


    def test_retrieve_factura(self):
        # Creamos una factura
        factura = Factura.objects.create(
            cliente=self.cliente,
            tipo_documento=self.tipo_documento,
            fecha_emision="2024-11-15",
            precio_total_venta=300000
        )
        url_detail = reverse('factura-detail', kwargs={'pk': factura.id_factura})
        response = self.client.get(url_detail)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_factura(self):
        # Creamos una factura existente
        factura = Factura.objects.create(
            cliente=self.cliente,
            tipo_documento=self.tipo_documento,
            fecha_emision="2024-11-15",
            precio_total_venta=300000
        )
        url_detail = reverse('factura-detail', kwargs={'pk': factura.id_factura})

        # Hacemos la solicitud DELETE
        response = self.client.delete(url_detail, content_type='application/json')
        print(response.status_code)
        print(response.data)

        # Verificamos el estado de la respuesta
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificamos que la factura ha sido eliminada
        with self.assertRaises(Factura.DoesNotExist):
            Factura.objects.get(id_factura=factura.id_factura)

