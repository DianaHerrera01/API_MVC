from django.urls import path
from .views import FacturaListCreateAPIView, FacturaRetrieveUpdateDestroyAPIView,  DetalleFacturaListCreateAPIView, DetalleFacturaRetrieveUpdateDestroyAPIView


urlpatterns = [
   
    # Rutas para Facturas
    path('facturas/', FacturaListCreateAPIView.as_view(), name='factura-list-create'),
    path('facturas/<int:pk>/', FacturaRetrieveUpdateDestroyAPIView.as_view(), name='factura-detail'),

     # Rutas para DetalleFactura
    path('detalle-facturas/', DetalleFacturaListCreateAPIView.as_view(), name='detallefactura-list-create'),
    path('detalle-facturas/<int:pk>/', DetalleFacturaRetrieveUpdateDestroyAPIView.as_view(), name='detallefactura-detail'),

]
