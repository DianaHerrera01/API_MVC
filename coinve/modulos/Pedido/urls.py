from django.urls import path
from .views import PedidoListCreateAPIView, PedidoRetrieveUpdateDestroyAPIView

urlpatterns = [
    # Rutas para Pedidos
    path('pedidos/', PedidoListCreateAPIView.as_view(), name='pedido-list-create'),
    path('pedidos/<int:pk>/', PedidoRetrieveUpdateDestroyAPIView.as_view(), name='pedido-detail'),
]
