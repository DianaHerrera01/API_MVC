from django.urls import path
from .views import (
    CategoriaListCreateAPIView, CategoriaRetrieveUpdateDestroyAPIView,
    ProductoListCreateAPIView, ProductoRetrieveUpdateDestroyAPIView,
    ProveedorListCreateAPIView, ProveedorRetrieveUpdateDestroyAPIView,
    ProductoServicioListCreateAPIView, ProductoServicioRetrieveUpdateDestroyAPIView,
    PedidoListCreateAPIView, PedidoRetrieveUpdateDestroyAPIView,
    EntradaListCreateAPIView, EntradaRetrieveUpdateDestroyAPIView,
    DevolucionListCreateAPIView, DevolucionRetrieveUpdateDestroyAPIView,
    TipoDocumentoListCreateAPIView, TipoDocumentoRetrieveUpdateDestroyAPIView,
    ClienteListCreateAPIView, ClienteRetrieveUpdateDestroyAPIView,
    FacturaListCreateAPIView, FacturaRetrieveUpdateDestroyAPIView,
    DetalleFacturaListCreateAPIView, DetalleFacturaRetrieveUpdateDestroyAPIView, 
    TipoNotaListCreateView, TipoNotaDetailView,
    NotaListCreateView, NotaDetailView, 
    ProductoNotaListCreateView,ProductoNotaDetailView,

)

urlpatterns = [
    # Endpoints para categorías
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroyAPIView.as_view(), name='categoria-detail'),

    # Endpoints para productos
    path('productos/', ProductoListCreateAPIView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto-detail'),

    # Rutas para Proveedores
    path('proveedores/', ProveedorListCreateAPIView.as_view(), name='proveedor-list-create'),
    path('proveedores/<int:pk>/', ProveedorRetrieveUpdateDestroyAPIView.as_view(), name='proveedor-detail'),

    # Rutas para ProductoServicio
    path('productoservicios/', ProductoServicioListCreateAPIView.as_view(), name='productoservicio-list-create'),
    path('productoservicios/<int:pk>/', ProductoServicioRetrieveUpdateDestroyAPIView.as_view(), name='productoservicio-detail'),

    # Rutas para Pedidos
    path('pedidos/', PedidoListCreateAPIView.as_view(), name='pedido-list-create'),
    path('pedidos/<int:pk>/', PedidoRetrieveUpdateDestroyAPIView.as_view(), name='pedido-detail'),

    # Rutas para Entradas
    path('entradas/', EntradaListCreateAPIView.as_view(), name='entrada-list-create'),
    path('entradas/<int:pk>/', EntradaRetrieveUpdateDestroyAPIView.as_view(), name='entrada-detail'),

    # Rutas para Devoluciones
    path('devoluciones/', DevolucionListCreateAPIView.as_view(), name='devolucion-list-create'),
    path('devoluciones/<int:pk>/', DevolucionRetrieveUpdateDestroyAPIView.as_view(), name='devolucion-detail'),

    # Rutas para Tipos de Documento
    path('tipos-documento/', TipoDocumentoListCreateAPIView.as_view(), name='tipo-documento-list-create'),
    path('tipos-documento/<int:pk>/', TipoDocumentoRetrieveUpdateDestroyAPIView.as_view(), name='tipo-documento-detail'),

    # Rutas para Clientes
    path('clientes/', ClienteListCreateAPIView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyAPIView.as_view(), name='cliente-detail'),

    # Rutas para Facturas
    path('facturas/', FacturaListCreateAPIView.as_view(), name='factura-list-create'),
    path('facturas/<int:pk>/', FacturaRetrieveUpdateDestroyAPIView.as_view(), name='factura-detail'),

    # Rutas para Detalles de Factura
    path('detalles-factura/', DetalleFacturaListCreateAPIView.as_view(), name='detalle-factura-list-create'),
    path('detalles-factura/<int:pk>/', DetalleFacturaRetrieveUpdateDestroyAPIView.as_view(), name='detalle-factura-detail'),

    # Rutas para Tipo Nota 
    path('tipo-notas/', TipoNotaListCreateView.as_view(), name='tipo-nota-list-create'),
    path('tipo-notas/<int:pk>/', TipoNotaDetailView.as_view(), name='tipo-nota-detail'),

    # Rutas para Nota
    path('notas/', NotaListCreateView.as_view(), name='nota-list-create'),
    path('notas/<int:pk>/', NotaDetailView.as_view(), name='nota-detail'),

    # Rutas para ProductoNota
    path('productos-notas/', ProductoNotaListCreateView.as_view(), name='producto-nota-list-create'),
    path('productos-notas/<int:pk>/', ProductoNotaDetailView.as_view(), name='producto-nota-detail'),

]
