from django.contrib import admin
from .models import Producto,Categoria

# Registra los modelos en el administrador
admin.site.register(Producto)
admin.site.register(Categoria)

