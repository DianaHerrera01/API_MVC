from rest_framework import generics
from .models import Factura, DetalleFactura
from .serializers import (
    FacturaSerializer, DetalleFacturaSerializer
)


# Factura Views
class FacturaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
class FacturaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

# DetalleFactura Views
class DetalleFacturaListCreateAPIView(generics.ListCreateAPIView):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer

class DetalleFacturaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer
