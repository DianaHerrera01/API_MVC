from rest_framework import generics
from .models import  Factura,  DetalleFactura
from .serializers import FacturaSerializer

# Factura Views
class FacturaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
