from django.urls import path
from .views import RegistroView, CustomTokenObtainPairView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),  # Para registro y listado de usuarios
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para autenticación
]
