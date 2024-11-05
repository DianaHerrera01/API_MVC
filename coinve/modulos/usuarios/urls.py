from django.urls import path
from .views import RegistroView, CustomTokenObtainPairView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),  # Para registro y listado de usuarios
    path('registro/<int:pk>/', RegistroView.as_view(), name='usuario_detalle'),  # Para editar, eliminar y obtener un usuario específico
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para autenticación
]
