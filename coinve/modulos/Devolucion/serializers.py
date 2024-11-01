from rest_framework import serializers
from .models import Devolucion
from modulos.producto.models import Producto
from modulos.proveedor.models import Proveedor

class DevolucionSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all())
    
    class Meta:
        model = Devolucion
        fields = [
            'id_devolucion',
            'proveedor',
            'producto',
            'cantidad',
            'motivo',
            'fecha_devolucion',
            'precio_unidad_compra',
            'precio_total_compra',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        #la representación de producto
        representation['producto'] = {
            "id_producto": instance.producto.id_producto,
            "nombre_producto": instance.producto.nombre_producto
        }
        
        # la representación de proveedor
        representation['proveedor'] = {
            "id_proveedor": instance.proveedor.id_proveedor,
            "nombre_proveedor": instance.proveedor.nombre_proveedor,
            "apellidos_proveedor": instance.proveedor.apellidos_proveedor
        }
        
        return representation
