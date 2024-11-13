from django.db import transaction
from rest_framework import serializers
from .models import Nota, TipoNota, ProductoNota
from modulos.producto.models import Producto
from modulos.factura.models import Factura
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
    productos = ProductoNotaSerializer(many=True, required=False)
    factura = serializers.PrimaryKeyRelatedField(queryset=Factura.objects.all())

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
        # incluir detalles adicionales de la factura
        if instance.factura:
            representation['factura'] = {
                "id_factura": instance.factura.id_factura,
                # puedes agregar otros campos de la factura aquí si los necesitas
            }

        return representation
    
    def create(self, validated_data):
        productos_data = validated_data.pop('productos', [])  # Extraemos la lista de productos (si existe)
        nota = Nota.objects.create(**validated_data)  # Creamos la instancia de la Nota

        # Si existen productos asociados
        if productos_data:
            # Crear los objetos ProductoNota y asociarlos a la nota creada
            for producto_data in productos_data:
                producto_nota = ProductoNota.objects.create(nota=nota, **producto_data)

                # Ajustar el stock del producto (sumar la cantidad)
                producto = producto_nota.producto  # Obtenemos el producto relacionado
                producto.cantidad += producto_nota.cantidad  # Sumar la cantidad vendida
                producto.save()  # Guardamos los cambios en el producto

        # Calcular el valor total de la nota (si es necesario)
        nota.valor = nota.calcular_valor()  # Llamamos al método para calcular el valor
        nota.save()  # Guardamos la nota con el valor actualizado

        return nota


    def update(self, instance, validated_data):
        productos_data = validated_data.pop('productos', None)  # Extraemos los productos si existen

        # Si se proporciona un valor manual, lo actualizamos directamente
        instance.valor = validated_data.get('valor', instance.valor)
        
        # Actualiza los otros campos de la nota
        instance.factura = validated_data.get('factura', instance.factura)
        instance.tipo_nota = validated_data.get('tipo_nota', instance.tipo_nota)
        instance.motivo = validated_data.get('motivo', instance.motivo)
        instance.save()  # Guardamos los cambios en la nota

        if productos_data is not None:
            # Restauramos las cantidades de los productos de los detalles anteriores
            for producto_nota in instance.productos.all():
                producto_nota.producto.cantidad += producto_nota.cantidad  # Devuelve la cantidad al inventario
                producto_nota.producto.save()  # Guardamos el producto actualizado

            # Eliminamos los productos anteriores de la nota
            instance.productos.all().delete()

            total = Decimal('0.00')  # Variable para almacenar el nuevo total

            # Procesamos los nuevos productos
            for producto_data in productos_data:
                producto = producto_data['producto']
                cantidad = producto_data['cantidad']

                # Actualiza la cantidad del producto (resta la nueva cantidad vendida)
                producto.cantidad -= cantidad  # Restamos la cantidad al inventario
                producto.save()  # Guardamos el producto actualizado

                # Recalculamos el valor de la nota sumando el valor de los productos
                total += producto.preciounidadventa * cantidad

                # Creamos el nuevo detalle de la factura
                ProductoNota.objects.create(nota=instance, producto=producto, cantidad=cantidad)

        # Si no se proporcionan productos y ya se ha establecido un valor manual, no recalculamos el valor
        # Solo se recalcula si productos_data está presente
        elif instance.valor == 0 and productos_data is None:
            instance.valor = validated_data.get('valor', instance.valor)
            instance.save()

         # Actualizamos el valor de la nota con el nuevo total
            instance.valor = total
            instance.save()

        return instance



