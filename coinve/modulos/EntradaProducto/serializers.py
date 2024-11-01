from rest_framework import serializers
from .models import Entrada
from modulos.Pedido.models import Pedido
from modulos.producto.models import Producto
from modulos.proveedor.models import Proveedor

# Serializador para Entrada
class EntradaSerializer(serializers.ModelSerializer): 
    pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all(), allow_null=True)
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all())

    class Meta:
        model = Entrada  
        fields = [
            'id_entrada',
            'pedido',
            'producto',
            'categoria',
            'proveedor',
            'cantidad',
            'fecha',
            'precio_total_compra',
            'precio_unidad_compra'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # la representación de producto
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