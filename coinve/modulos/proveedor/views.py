from rest_framework import generics
from .models import Proveedor
from .serializers import ProveedorSerializer

# Proveedor Views
class ProveedorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
