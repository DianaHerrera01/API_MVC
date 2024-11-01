from rest_framework import serializers
from modulos.proveedor.models import Proveedor
from .models import Producto, Categoria

# Serializador para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoriaID', 'nom_categoria']

# Serializador para Producto
class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all())

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Modificar la representación de categoria para mostrar id y nom_categoria
        if instance.categoria:
            representation['categoria'] = {
                "categoriaID": instance.categoria.categoriaID,
                "nom_categoria": instance.categoria.nom_categoria
            }
        
        # Modificar la representación de proveedor para mostrar id, nombre y apellido
        if instance.proveedor:
            representation['proveedor'] = {
                "id_proveedor": instance.proveedor.id_proveedor,
                "nombre_proveedor": instance.proveedor.nombre_proveedor,
                "apellidos_proveedor": instance.proveedor.apellidos_proveedor
            }
        
        return representation
    
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
