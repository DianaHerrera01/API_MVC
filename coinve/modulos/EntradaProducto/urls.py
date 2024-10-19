from django.urls import path
from .views import EntradaListCreateAPIView, EntradaRetrieveUpdateDestroyAPIView

urlpatterns = [

    # Rutas para Entradas
    path('entradas/', EntradaListCreateAPIView.as_view(), name='entrada-list-create'),
    path('entradas/<int:pk>/', EntradaRetrieveUpdateDestroyAPIView.as_view(), name='entrada-detail'),
]
