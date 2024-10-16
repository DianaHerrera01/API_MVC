from rest_framework import generics
from .models import (
    Producto, 
    Categoria, 
    Proveedor, 
    ProductoServicio, 
    Pedido, 
    Entrada, 
    Devolucion, 
    TipoDocumento, 
    Cliente, 
    Factura, 
    DetalleFactura, TipoNota, 
    Nota, 
    ProductoNota

)
from .serializers import (
    ProductoSerializer, 
    CategoriaSerializer, 
    ProveedorSerializer, 
    ProductoServicioSerializer, 
    PedidoSerializer, 
    EntradaSerializer, 
    DevolucionSerializer, 
    TipoDocumentoSerializer, 
    ClienteSerializer, 
    FacturaSerializer, 
    DetalleFacturaSerializer, 
    TipoNotaSerializer, 
    NotaSerializer, 
    ProductoNotaSerializer
)

# Categoría Views
class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Producto Views
class ProductoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

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

# Pedido Views
class PedidoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Entrada Views
class EntradaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class EntradaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

# Devolución Views
class DevolucionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

class DevolucionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

# Tipo Documento Views
class TipoDocumentoListCreateAPIView(generics.ListCreateAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer

class TipoDocumentoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer

# Cliente Views
class ClienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Factura Views
class FacturaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

# Detalle Factura Views
class DetalleFacturaListCreateAPIView(generics.ListCreateAPIView):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer

class DetalleFacturaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer

# Tipo Nota Views
class TipoNotaListCreateView(generics.ListCreateAPIView):
    queryset = TipoNota.objects.all()
    serializer_class = TipoNotaSerializer

class TipoNotaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoNota.objects.all()
    serializer_class = TipoNotaSerializer

# Nota Views
class NotaListCreateView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

class NotaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

# ProductoNota Views
class ProductoNotaListCreateView(generics.ListCreateAPIView):
    queryset = ProductoNota.objects.all()
    serializer_class = ProductoNotaSerializer

class ProductoNotaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductoNota.objects.all()
    serializer_class = ProductoNotaSerializer