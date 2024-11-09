from django.urls import path
from .views import (
    ProveedorListCreateAPIView, ProveedorRetrieveUpdateDestroyAPIView, 
    ProductoServicioListCreateAPIView, ProductoServicioRetrieveUpdateDestroyAPIView
)

urlpatterns = [
   
    # Rutas para Proveedores
    path('proveedores/', ProveedorListCreateAPIView.as_view(), name='proveedor-list-create'),
    path('proveedores/<int:pk>/', ProveedorRetrieveUpdateDestroyAPIView.as_view(), name='proveedor-detail'),

     # Rutas para ProductoServicio
    path('productos-servicios/', ProductoServicioListCreateAPIView.as_view(), name='producto-servicio-list-create'),
    path('productos-servicios/<int:pk>/', ProductoServicioRetrieveUpdateDestroyAPIView.as_view(), name='producto-servicio-detail'),
]
