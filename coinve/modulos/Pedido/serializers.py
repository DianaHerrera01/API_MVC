from rest_framework import serializers
from .models import Pedido
from modulos.producto.models import Producto
from modulos.proveedor.models import Proveedor

# Serializador para Pedido
class PedidoSerializer(serializers.ModelSerializer): 
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all())

    class Meta:
        model = Pedido 
        fields = [
            'id_orden_pedido',
            'proveedor',
            'producto',
            'cantidad',
            'estado'
        ]