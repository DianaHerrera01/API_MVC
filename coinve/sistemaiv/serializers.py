from rest_framework import serializers
from .models import (
    Producto,
    Categoria,
    Proveedor,
    ProductoServicio,
    Pedido,
    Entrada,
    Devolucion,
    TipoDocumento,
    Cliente,
    Factura,
    DetalleFactura,
    TipoNota, Nota, ProductoNota
)

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

# Serializador para Pedido
class PedidoSerializer(serializers.ModelSerializer): 
    producto = ProductoSerializer()
    proveedor = ProveedorSerializer()

    class Meta:
        model = Pedido 
        fields = [
            'id_orden_pedido',
            'proveedor',
            'producto',
            'cantidad',
            'estado'
        ]

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

# Serializador para Devolucion
class DevolucionSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()  # Serializador para el producto
    proveedor = ProveedorSerializer()

    class Meta:
        model = Devolucion
        fields = [
            'id_devolucion',
            'proveedor',
            'producto',
            'cantidad',
            'motivo',
            'fecha_devolucion',
            'precio_unidad_compra',
            'precio_total_compra',
        ]

# Serializador para TipoDocumento
class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ['id_tipo_docum', 'nom_tipo_doc']

# Serializador para Cliente
class ClienteSerializer(serializers.ModelSerializer):
    tipo_documento = TipoDocumentoSerializer()

    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nombre_cliente',
            'apellidos_cliente',
            'correo',
            'tipo_documento',
            'telefono'
        ]

# Serializador para DetalleFactura
class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = DetalleFactura
        fields = [
            'producto',
            'cantidad',
            'precio_unidad_venta',
            'precio_total_venta'
        ]

# Serializador para Factura
class FacturaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    detalles = DetalleFacturaSerializer(many=True, source='detallefactura_set')  # Relación inversa

    class Meta:
        model = Factura
        fields = [
            'id_factura',
            'cliente',
            'tipo_documento',
            'numero_documento',
            'fecha_emision',
            'precio_total_venta',
            'actividad_comercial',
            'nit',
            'nombre_negocio',
            'detalles'  # Agregar detalles de la factura
        ]

# Serializador para TipoNota, Nota, ProductoNota

class TipoNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNota
        fields = ['id_tipo_nota', 'nom_nota']

class NotaSerializer(serializers.ModelSerializer):
    productos = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        required=False,  # Esto hace que el campo no sea obligatorio
        allow_empty=True  # Permite que se envíe una lista vacía
    )

    class Meta:
        model = Nota
        fields = ['id_nota', 'factura', 'motivo', 'tipo_nota', 'valor', 'productos']

class ProductoNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoNota
        fields = ['producto', 'nota', 'cantidad']