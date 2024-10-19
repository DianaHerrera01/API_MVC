from django.db import models
from modulos.proveedor.models import Proveedor

# Modelos de Producto y Categoria
class Categoria(models.Model):
    categoriaID = models.AutoField(primary_key=True)
    nom_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    preciounidadcompra = models.DecimalField(max_digits=10, decimal_places=2)
    preciounidadventa = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_producto
