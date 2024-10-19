from django.urls import path
from .views import DevolucionListCreateAPIView, DevolucionRetrieveUpdateDestroyAPIView
   
urlpatterns = [

    # Rutas para Devoluciones
    path('devoluciones/', DevolucionListCreateAPIView.as_view(), name='devolucion-list-create'),
    path('devoluciones/<int:pk>/', DevolucionRetrieveUpdateDestroyAPIView.as_view(), name='devolucion-detail'),

]
