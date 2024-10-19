from rest_framework import generics
from .models import Devolucion
from .serializers import DevolucionSerializer

class DevolucionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

class DevolucionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer
