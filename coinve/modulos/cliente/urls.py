from django.urls import path
from .views import (
    TipoDocumentoListCreateAPIView, TipoDocumentoRetrieveUpdateDestroyAPIView,
    ClienteListCreateAPIView, ClienteRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    
    # Rutas para Tipos de Documento
    path('tipos-documento/', TipoDocumentoListCreateAPIView.as_view(), name='tipo-documento-list-create'),
    path('tipos-documento/<int:pk>/', TipoDocumentoRetrieveUpdateDestroyAPIView.as_view(), name='tipo-documento-detail'),

    # Rutas para Clientes
    path('clientes/', ClienteListCreateAPIView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyAPIView.as_view(), name='cliente-detail'),

]