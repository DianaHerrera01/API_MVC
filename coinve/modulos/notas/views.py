from rest_framework import generics
from modulos.notas.models import Nota, TipoNota
from .serializers import NotaSerializer, TipoNotaSerializer

# TipoNota Views
class TipoNotaListCreateAPIView(generics.ListCreateAPIView):
    queryset = TipoNota.objects.all()
    serializer_class = TipoNotaSerializer

class TipoNotaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoNota.objects.all()
    serializer_class = TipoNotaSerializer

# Nota Views
class NotaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

class NotaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


