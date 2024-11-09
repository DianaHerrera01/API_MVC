from rest_framework import serializers
from .models import Proveedor, ProductoServicio

# Serializador para ProductoServicio
class ProductoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = [
            'id_producto_servicio',
            'nom_producto_serv'
        ]

# Serializador para Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    productos_servicios = serializers.PrimaryKeyRelatedField(
        queryset=ProductoServicio.objects.all(),
        many=True
    )
   
    class Meta:
        model = Proveedor
        fields = [
            'id_proveedor',
            'nombre_proveedor', 
            'apellidos_proveedor', 
            'correo', 
            'direccion', 
            'telefono',
            'productos_servicios'
        ]
    
    def to_representation(self, instance):
        # Llamar al método padre para obtener la representación original
        representation = super().to_representation(instance)

        # Personalizar la representación de productos_servicios
        productos_servicios_representation = []
        for producto in instance.productos_servicios.all():
            productos_servicios_representation.append({
                "id_producto_servicio": producto.id_producto_servicio,
                "nom_producto_serv": producto.nom_producto_serv
            })

        # Reemplazar la lista de IDs con los detalles de los productos
        representation['productos_servicios'] = productos_servicios_representation

        return representation

    def create(self, validated_data):
        productos_servicios_data = validated_data.pop('productos_servicios', [])
        proveedor = Proveedor.objects.create(**validated_data)
        proveedor.productos_servicios.set(productos_servicios_data)
        return proveedor

    def update(self, instance, validated_data):
        productos_servicios_data = validated_data.pop('productos_servicios', [])
        instance = super().update(instance, validated_data)
        instance.productos_servicios.set(productos_servicios_data)
        return instance
    