from rest_framework import serializers
from .models import Proveedor, ProductoServicio

# Serializador para ProductoServicio
class ProductoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = ['id_producto_servicio', 'nom_producto_servicio']

# Serializador para Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    productos_servicio = ProductoServicioSerializer(many=True, read_only=True, source='productos')

    class Meta:
        model = Proveedor
        fields = [
            'id_proveedor',
            'nombre_proveedor', 
            'apellidos_proveedor', 
            'correo', 
            'direccion', 
            'telefono', 
            'productos_servicio'  # Incluir productos_servicio
        ]