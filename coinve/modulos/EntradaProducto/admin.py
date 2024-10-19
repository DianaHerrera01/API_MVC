from django.contrib import admin


from .models import Entrada # Importa los modelos

# Registra los modelos en el administrador
admin.site.register(Entrada)