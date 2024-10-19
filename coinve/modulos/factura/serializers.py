from rest_framework import serializers
from .models import Factura, DetalleFactura
from modulos.producto.models import Producto
from modulos.cliente.models import Cliente  

# Serializador para DetalleFactura
class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = ['producto', 'cantidad', 'precio_total_venta']

# Serializador para Factura
class FacturaSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    detalles = DetalleFacturaSerializer(many=True, write_only=True)  # Usamos el nuevo serializador
    documento_cli = serializers.CharField(source='cliente.documento_cli', read_only=True)

    class Meta:
        model = Factura
        fields = [
            'id_factura',
            'nombre_negocio',
            'actividad_comercial',
            'nit',
            'cliente',
            'tipo_documento',
            'documento_cli',
            'fecha_emision',
            'precio_total_venta',
            'detalles',  # Usamos el serializador de detalles
        ]

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles', [])
        factura = Factura.objects.create(**validated_data)

        total_venta = 0
        for detalle in detalles_data:
            producto_id = detalle.pop('producto')  # Extrae el ID del producto
            producto = Producto.objects.get(id_producto=producto_id)  # Obtiene el producto
            cantidad = detalle['cantidad']
            precio_unidad_venta = producto.preciounidadventa
            precio_total_venta = cantidad * precio_unidad_venta  # Calcula el precio total

            # Guarda el detalle de la factura
            DetalleFactura.objects.create(
                factura=factura,
                producto=producto,
                cantidad=cantidad,
                precio_unidad_venta=precio_unidad_venta,
                precio_total_venta=precio_total_venta
            )
            total_venta += precio_total_venta
            
            # Ajustar cantidad en el producto
            producto.cantidad -= cantidad
            producto.save()

        factura.precio_total_venta = total_venta
        factura.save()
        
        return factura

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Obtener todos los detalles de la factura usando el serializador DetalleFacturaSerializer
        detalles = DetalleFactura.objects.filter(factura=instance)
        detalles_serializados = DetalleFacturaSerializer(detalles, many=True).data
        
        representation['detalles'] = detalles_serializados
        return representation