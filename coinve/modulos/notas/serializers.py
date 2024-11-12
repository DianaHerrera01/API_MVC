from django.db import transaction
from rest_framework import serializers
from .models import Nota, TipoNota, ProductoNota
from modulos.producto.models import Producto
from decimal import Decimal

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

        with transaction.atomic():
            # Crear los objetos ProductoNota y asociarlos a la nota creada
            for producto_data in productos_data:
                producto_nota = ProductoNota.objects.create(nota=nota, **producto_data)

                # Ajustar el stock en el momento de la creación
                if nota.tipo_nota.nom_nota.lower() == "nota de credito":
                    producto_nota.producto.cantidad += producto_nota.cantidad
                    producto_nota.producto.save()

            # Calcular el valor de la nota
            nota.valor = nota.calcular_valor()
            nota.save()

        return nota
    
   
    def update(self, instance, validated_data):
        productos_data = validated_data.pop('productos', None)

        # Actualiza los campos de la nota
        instance.factura = validated_data.get('factura', instance.factura)
        instance.tipo_nota = validated_data.get('tipo_nota', instance.tipo_nota)
        instance.motivo = validated_data.get('motivo', instance.motivo)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.save()

        if productos_data is not None:
            # Restauramos las cantidades de los productos de los detalles existentes
            for producto_nota in instance.productos.all():
                producto_nota.producto.cantidad += producto_nota.cantidad  # Devuelve la cantidad al inventario
                producto_nota.producto.save()  # Guarda el producto actualizado

            # Eliminamos los productos anteriores de la nota
            instance.productos.all().delete()

            total = Decimal('0.00')  # Variable para calcular el nuevo total

            # Procesamos los nuevos productos
            for producto_data in productos_data:
                producto = producto_data['producto']
                cantidad = producto_data['cantidad']

                # Actualiza la cantidad del producto (resta la nueva cantidad vendida)
                producto.cantidad -= cantidad
                producto.save()  # Guarda el producto actualizado

                # Recalculamos el valor de la nota sumando el valor de los productos
                total += producto.preciounidadventa * cantidad

                # Crea el nuevo detalle de la factura
                ProductoNota.objects.create(nota=instance, producto=producto, cantidad=cantidad)

            # Actualiza el valor de la nota
            instance.valor = total
            instance.save()

        return instance

