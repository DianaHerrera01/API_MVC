from django.contrib import admin
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
)

# Registra los modelos en el administrador
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(ProductoServicio)
admin.site.register(Pedido)
admin.site.register(Entrada)
admin.site.register(Devolucion)
admin.site.register(TipoDocumento)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
