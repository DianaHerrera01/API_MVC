from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistroSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Registro de usuario
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid(): # verificar si los datos son válidos según el serializador
            user = serializer.save()
            # retornar una respuesta con los datos del usuario registrado y un mensaje de éxito
            return Response({
                "mensaje": "Usuario registrado correctamente.",
                "usuario": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "password": request.data.get('password') 
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # consultar todos los usuarios registrados en la base de datos
        usuarios = User.objects.all()
        usuarios_data = [
            {
                "id": usuario.id,
                "username": usuario.username,
                "email": usuario.email,
                "first_name": usuario.first_name,
                "last_name": usuario.last_name,
                "password": request.data.get('password')  
            }
            for usuario in usuarios
        ]
        return Response(usuarios_data, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs): # llamar al método post de la clase padre para obtener el token
        response = super().post(request, *args, **kwargs)
        response.data['mensaje'] = "Autenticación satisfactoria."  # retornar la respuesta con el token y el mensaje
        return response

