from rest_framework import serializers
from .models import Proveedor


# Serializador para Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Proveedor
        fields = [
            'id_proveedor',
            'nombre_proveedor', 
            'apellidos_proveedor', 
            'correo', 
            'direccion', 
            'telefono'
        ]