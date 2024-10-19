from rest_framework import generics
from .models import Entrada
from .serializers import EntradaSerializer

# Entrada Views
class EntradaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class EntradaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
