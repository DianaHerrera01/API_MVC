from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    apellidos_proveedor = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)


    def __str__(self):
        return self.nombre_proveedor

class ProductoServicio(models.Model):
    id_producto_servicio = models.AutoField(primary_key=True)
    nom_producto_serv = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, related_name='productos_servicios', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nom_producto_serv