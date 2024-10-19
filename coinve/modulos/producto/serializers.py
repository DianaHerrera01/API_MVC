from rest_framework import serializers
from modulos.proveedor.models import Proveedor
from .models import Producto,Categoria

# Serializador para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoriaID', 'nom_categoria']

# Serializador para Producto
class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all(), required=False)
    
    class Meta:
        model = Producto
        fields = [
            'id_producto', 
            'nombre_producto', 
            'cantidad', 
            'categoria', 
            'descripcion', 
            'proveedor',  # Incluir el proveedor
            'preciounidadcompra', 
            'preciounidadventa'
        ]

