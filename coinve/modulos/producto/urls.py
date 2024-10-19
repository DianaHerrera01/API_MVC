from django.urls import path
from .views import (
    CategoriaListCreateAPIView, CategoriaRetrieveUpdateDestroyAPIView,
    ProductoListCreateAPIView, ProductoRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Endpoints para categorías
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroyAPIView.as_view(), name='categoria-detail'),

    # Endpoints para productos
    path('productos/', ProductoListCreateAPIView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto-detail'),

]
