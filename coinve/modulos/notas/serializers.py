from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Nota, TipoNota, ProductoNota
from modulos.producto.models import Producto

class TipoNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNota
        fields = ['id_tipo_nota', 'nom_nota']

class ProductoNotaSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

    class Meta:
        model = ProductoNota
        fields = ['producto', 'cantidad']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Modificar la representación de producto
        representation['producto'] = {
            "id_producto": instance.producto.id_producto,
            "nombre_producto": instance.producto.nombre_producto
        }
        
        return representation

class NotaSerializer(serializers.ModelSerializer):
    tipo_nota = serializers.PrimaryKeyRelatedField(queryset=TipoNota.objects.all())
    productos = ProductoNotaSerializer(many=True)

    class Meta:
        model = Nota
        fields = ['id_nota', 'factura','tipo_nota', 'motivo', 'valor', 'productos']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # representación de tipo_nota para mostrar id_tipo_nota y nom_nota
        if instance.tipo_nota: 
            representation['tipo_nota'] = {
                "id_tipo_nota": instance.tipo_nota.id_tipo_nota,
                "nom_nota": instance.tipo_nota.nom_nota
            }
        
        return representation
    
    def create(self, validated_data):
        productos_data = validated_data.pop('productos')  # Obtener los datos de los productos
        nota = Nota.objects.create(**validated_data)  # Crear la instancia de la Nota
            
        # Crear los objetos ProductoNota y asociarlos a la nota creada
        for producto_data in productos_data:
            ProductoNota.objects.create(nota=nota, **producto_data)
            
        # Calcular el valor de la nota
        nota.valor = nota.calcular_valor()
        nota.save()
                
        return nota
    
    """
    def update(self, instance, validated_data):
        # Actualiza la cantidad del producto
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        instance.save()

        # Después de guardar la instancia de ProductoNota, actualizamos el stock
        if instance.producto and instance.cantidad:
            # Ajustamos el stock según el tipo de nota (crédito o débito)
            if instance.nota.tipo_nota.nom_nota.lower() == "nota de crédito":
                # Aumentar el stock para la nota de crédito
                instance.producto.cantidad += instance.cantidad
            elif instance.nota.tipo_nota.nom_nota.lower() == "nota de débito":
                # Disminuir el stock para la nota de débito
                if instance.producto.cantidad < instance.cantidad:
                    raise ValueError("No hay suficiente stock.")
                instance.producto.cantidad -= instance.cantidad
            # Guardamos el cambio en el producto
            instance.producto.save()

        return instance
    """