from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from modulos.factura.models import Factura
from modulos.producto.models import Producto

# Definir la clase ProductoNota primero
class ProductoNota(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)  # Producto opcional
    nota = models.ForeignKey('Nota', on_delete=models.CASCADE, related_name='productos')  # Nota asociada
    cantidad = models.PositiveIntegerField(null=True, blank=True)  # Cantidad opcional

    def __str__(self):
        if self.producto:
            return f"Producto: {self.producto.nombre_producto} - Nota: {self.nota.id_nota}"
        return f"Nota sin producto asociado - Nota: {self.nota.id_nota}"

    def save(self, *args, **kwargs):
        # Llamar al método save original
        super(ProductoNota, self).save(*args, **kwargs)


class Nota(models.Model):
    id_nota = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    motivo = models.TextField()
    tipo_nota = models.ForeignKey('TipoNota', on_delete=models.CASCADE,)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Nota {self.id_nota} - Factura {self.factura.id_factura}"
    
    def calcular_valor(self):
        # Si ya se tiene un valor manual definido, usar ese valor
        if self.valor > 0:
            return self.valor  # Si ya se definió un valor manual, devolverlo

        # Si no hay productos asociados, retornar el valor manual
        if not self.productos.exists():
            return self.valor

        # Calcular el valor de la nota sumando el valor de cada producto
        total_valor = sum([producto_nota.producto.preciounidadventa * producto_nota.cantidad for producto_nota 
                           in self.productos.all()])
        return total_valor


@receiver(post_save, sender=ProductoNota)
def actualizar_valor_nota(sender, instance, created, **kwargs):
    if created:  # Solo cuando se crea un nuevo ProductoNota
        instance.nota.valor = instance.nota.calcular_valor()
        instance.nota.save()
    else:
        # Si la cantidad del producto cambia, también recalcular el valor de la nota
        instance.nota.valor = instance.nota.calcular_valor()
        instance.nota.save()


class TipoNota(models.Model):
    id_tipo_nota = models.AutoField(primary_key=True)
    nom_nota = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_nota
