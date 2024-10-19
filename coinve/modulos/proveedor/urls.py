from django.urls import path
from .views import (
    ProveedorListCreateAPIView, ProveedorRetrieveUpdateDestroyAPIView,
    ProductoServicioListCreateAPIView, ProductoServicioRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
   
    # Rutas para Proveedores
    path('proveedores/', ProveedorListCreateAPIView.as_view(), name='proveedor-list-create'),
    path('proveedores/<int:pk>/', ProveedorRetrieveUpdateDestroyAPIView.as_view(), name='proveedor-detail'),

    # Rutas para ProductoServicio
    path('productoservicios/', ProductoServicioListCreateAPIView.as_view(), name='productoservicio-list-create'),
    path('productoservicios/<int:pk>/', ProductoServicioRetrieveUpdateDestroyAPIView.as_view(), name='productoservicio-detail'),
    
]
