from rest_framework import generics
from .models import Proveedor, ProductoServicio
from .serializers import ProveedorSerializer, ProductoServicioSerializer

# Proveedor Views
class ProveedorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# Producto Servicio Views
class ProductoServicioListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

class ProductoServicioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

