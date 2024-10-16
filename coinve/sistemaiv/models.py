from django.db import models

# Modelos de Proveedor
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
    nom_producto_servicio = models.CharField(max_length=100)
    # Relación Many-to-Many con proveedores, un producto/servicio puede tener varios proveedores
    proveedores = models.ManyToManyField(Proveedor, related_name='productos')  

    def __str__(self):
        return self.nom_producto_servicio

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

# Modelos de Pedido
class Pedido(models.Model):
    # Definimos los posibles estados que puede tener un pedido
    ESTADOS_PEDIDO = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Recibido', 'Recibido'),
    ]
    id_orden_pedido = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
     # Estado del pedido, con opciones limitadas a los valores definidos en ESTADOS_PEDIDO
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='Pendiente')

    def __str__(self):
        return f"Pedido {self.id_orden_pedido} - {self.producto.nombre_producto} ({self.cantidad})"


# Modelos de Entrada
class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    # SET_NULL para que la entrada no sea eliminada cuando el pedido sea eliminado
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True) 
    # PROTECT para evitar que el producto se elimine si está asociado a una entrada 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    precio_total_compra = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_unidad_compra = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Entrada de {self.producto.nombre_producto} - {self.cantidad}"

    # Sobrescritura del método save para calcular automáticamente el precio total y actualizar el inventario
    def save(self, *args, **kwargs):
        if self.precio_unidad_compra is None:
            self.precio_unidad_compra = self.producto.preciounidadcompra

        self.cantidad = int(self.cantidad)
        self.precio_total_compra = self.precio_unidad_compra * self.cantidad

        self.producto.cantidad += self.cantidad
        self.producto.preciounidadcompra = self.precio_unidad_compra
        self.producto.save()

        super().save(*args, **kwargs)


# Modelos de Devolución
class Devolucion(models.Model):
    id_devolucion = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    motivo = models.TextField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(auto_now_add=True)

    # Propiedad que obtiene el precio de compra por unidad del producto devuelto
    @property
    def precio_unidad_compra(self):
        return self.producto.preciounidadcompra if self.producto else 0

    # Propiedad que calcula el precio total de la devolución
    @property
    def precio_total_compra(self):
        return self.precio_unidad_compra * self.cantidad

    @property
    def nombre_proveedor(self):
        return self.producto.proveedor.nombre_proveedor if self.producto.proveedor else "Sin proveedor"

    @property
    def apellidos_proveedor(self):
        return self.producto.proveedor.apellidos_proveedor if self.producto.proveedor else "Sin apellidos"

    def __str__(self):
        return f"Devolución de {self.cantidad} {self.producto.nombre_producto} a {self.nombre_proveedor} {self.apellidos_proveedor}"


# Modelos de Cliente y TipoDocumento
class TipoDocumento(models.Model):
    id_tipo_docum = models.AutoField(primary_key=True)
    nom_tipo_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_tipo_doc

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellidos_cliente = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    id_tipo_docum = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento_cli = models.CharField(max_length=11)  
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellidos_cliente}"


# Modelos de Factura y DetalleFactura
class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=11, default='' )
    fecha_emision = models.DateField()
    precio_total_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actividad_comercial = models.CharField(max_length=255, default="Comercio al por menor de computadores, equipos periféricos y equipo de telecomunicaciones.")
    nit = models.CharField(max_length=15, default="700668550-5")
    nombre_negocio = models.CharField(max_length=100, default="TEGNOFACIL")

    def __str__(self):
        return f"Factura {self.id_factura} - {self.cliente.nombre_cliente} {self.cliente.apellidos_cliente}"

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unidad_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.producto.nombre_producto} ({self.cantidad})"
    
# Modelos de TipoNota, Nota, ProductoNota

class TipoNota(models.Model):
    id_tipo_nota = models.AutoField(primary_key=True)
    nom_nota = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_nota

class Nota(models.Model):
    id_nota = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    motivo = models.TextField()
    tipo_nota = models.ForeignKey(TipoNota, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    productos = models.ManyToManyField(Producto, through='ProductoNota')

    def __str__(self):
        return f"Nota {self.id_nota} - Factura {self.factura.id_factura}"

class ProductoNota(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)  # Producto opcional
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(null=True, blank=True)  # Cantidad opcional

    def __str__(self):
        if self.producto:
            return f"Producto: {self.producto.nombre_producto} - Nota: {self.nota.id_nota}"
        return f"Nota sin producto asociado - Nota: {self.nota.id_nota}"
    
     # Sobreescribe el método save para gestionar actualizaciones de stock y factura.
    def save(self, *args, **kwargs):
        # Llamar al método save original primero para asegurarnos de que la nota existe
        super(ProductoNota, self).save(*args, **kwargs)

        # Verifica si el producto y la cantidad están definidos.
        if self.producto and self.cantidad:
            subtotal = self.producto.preciounidadventa * self.cantidad  # Calcular subtotal

            # Ajustar el stock del producto y el total de la factura
            if self.nota.tipo_nota.nom_nota.lower() == "nota de crédito":
                # Devolución del producto - aumentar stock y disminuir total de factura
                self.producto.cantidad += self.cantidad
                self.nota.factura.precio_total_venta -= subtotal
                
            elif self.nota.tipo_nota.nom_nota.lower() == "nota de débito":
                # Venta adicional - disminuir stock y aumentar total de factura
                if self.producto.cantidad < self.cantidad:
                    raise ValueError("No hay suficiente stock para vender este producto.")
                self.producto.cantidad -= self.cantidad
                self.nota.factura.precio_total_venta += subtotal

            self.producto.save()
            self.nota.factura.save()

            # Actualizar la cantidad en la factura
            detalle_factura = self.nota.factura.detallefactura_set.filter(producto=self.producto).first()
            if detalle_factura:
                if self.nota.tipo_nota.nom_nota.lower() == "nota de crédito":
                    # Disminuir cantidad en la factura
                    detalle_factura.cantidad -= self.cantidad
                elif self.nota.tipo_nota.nom_nota.lower() == "nota de débito":
                    # Aumentar cantidad en la factura
                    detalle_factura.cantidad += self.cantidad
                detalle_factura.save()
