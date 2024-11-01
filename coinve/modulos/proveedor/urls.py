from django.urls import path
from .views import (
    ProveedorListCreateAPIView, ProveedorRetrieveUpdateDestroyAPIView
)

urlpatterns = [
   
    # Rutas para Proveedores
    path('proveedores/', ProveedorListCreateAPIView.as_view(), name='proveedor-list-create'),
    path('proveedores/<int:pk>/', ProveedorRetrieveUpdateDestroyAPIView.as_view(), name='proveedor-detail'),
]
