from django.urls import path
from .views import (
    TipoNotaListCreateAPIView,
    TipoNotaRetrieveUpdateDestroyAPIView,
    NotaListCreateAPIView,
    NotaRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # TipoNota URLs
    path('tipo-nota/', TipoNotaListCreateAPIView.as_view(), name='tipo-nota-list-create'),
    path('tipo-nota/<int:pk>/', TipoNotaRetrieveUpdateDestroyAPIView.as_view(), name='tipo-nota-retrieve-update-destroy'),

    # Nota URLs
    path('nota/', NotaListCreateAPIView.as_view(), name='nota-list-create'),
    path('nota/<int:pk>/', NotaRetrieveUpdateDestroyAPIView.as_view(), name='nota-retrieve-update-destroy'),

]