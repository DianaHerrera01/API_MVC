from rest_framework import serializers
from .models import Entrada
from modulos.Pedido.models import Pedido

# Serializador para Entrada
class EntradaSerializer(serializers.ModelSerializer): 
    pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all())

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
