from rest_framework import serializers
from .models import Factura, DetalleFactura
from modulos.cliente.models import Cliente, TipoDocumento
from modulos.producto.models import Producto
from decimal import Decimal

class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

    class Meta:
        model = DetalleFactura
        fields = ['producto', 'cantidad', 'precio_total_venta']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Modificar la representación de producto
        representation['producto'] = {
            "id_producto": instance.producto.id_producto,
            "nombre_producto": instance.producto.nombre_producto
        }
        
        return representation

class FacturaSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    tipo_documento = serializers.PrimaryKeyRelatedField(queryset=TipoDocumento.objects.all()) 
    detalles = DetalleFacturaSerializer(many=True)
    numero_documento = serializers.CharField(source='cliente.documento_cli', read_only=True)
    
    class Meta:
        model = Factura
        fields = [
            'id_factura',
            'cliente',
            'tipo_documento',
            'numero_documento',
            'fecha_emision',
            'precio_total_venta',
            'actividad_comercial',
            'nit',
            'nombre_negocio',
            'detalles'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Modificar la representación de cliente para mostrar nombre y apellidos
        if instance.cliente:
            representation['cliente'] = {
                "id_cliente": instance.cliente.id_cliente,
                "nombre_cliente": instance.cliente.nombre_cliente,
                "apellidos_cliente": instance.cliente.apellidos_cliente
            }

        # Modificar la representación de tipo_documento para mostrar nombre o descripción
        if instance.tipo_documento:
            representation['tipo_documento'] = {
                "id_tipo_docum": instance.tipo_documento.id_tipo_docum,
                "nom_tipo_doc": instance.tipo_documento.nom_tipo_doc  # Asegúrate de usar el campo correcto
            }
        
        return representation
    

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        factura = Factura(**validated_data)
        factura.save()  # Guarda la factura primero

        total = 0  # Inicializa la variable para calcular el total
        for detalle_data in detalles_data:
            producto = detalle_data['producto']
            cantidad = detalle_data['cantidad']

            # Actualiza la cantidad del producto (resta la cantidad vendida)
            producto.cantidad -= cantidad  # Cambia esto según el campo de cantidad que tengas
            producto.save()  # Guarda el producto actualizado

            # Crea el detalle de la factura
            detalle = DetalleFactura(**detalle_data, factura=factura)
            detalle.save()  # Guarda el detalle
            total += detalle.precio_total_venta  # Suma el precio total del detalle

        factura.precio_total_venta = total  # Asigna el total calculado
        factura.save()  # Guarda la factura nuevamente con el total actualizado
        return factura

    def update(self, instance, validated_data):
        detalles_data = validated_data.pop('detalles', None)

        # Actualiza la instancia de la factura
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.tipo_documento = validated_data.get('tipo_documento', instance.tipo_documento)
        instance.numero_documento = validated_data.get('numero_documento', instance.numero_documento)
        instance.fecha_emision = validated_data.get('fecha_emision', instance.fecha_emision)
        instance.save()

        # Restaura la cantidad de productos en los detalles actuales
        if detalles_data is not None:
            # Restaura la cantidad de los productos de los detalles existentes
            for detalle in instance.detalles.all():
                detalle.producto.cantidad += detalle.cantidad  # Devuelve la cantidad al inventario
                detalle.producto.save()  # Guarda el producto actualizado

            # Elimina los detalles existentes
            instance.detalles.all().delete()  

            total = Decimal('0.00')  # Variable para calcular el nuevo total
            for detalle_data in detalles_data:
                producto = detalle_data['producto']
                cantidad = detalle_data['cantidad']

                # Actualiza la cantidad del producto (resta la nueva cantidad vendida)
                producto.cantidad -= cantidad  # Cambia esto según el campo de cantidad que tengas
                producto.save()  # Guarda el producto actualizado

                # Crea el nuevo detalle de la factura
                detalle = DetalleFactura.objects.create(factura=instance, **detalle_data)
                total += detalle.precio_total_venta  # Suma el precio total del nuevo detalle

            instance.precio_total_venta = total  # Asigna el nuevo total calculado
            instance.save()  # Guarda la factura actualizada

        return instance