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
