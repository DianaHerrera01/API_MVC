from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.password_validation import validate_password
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

    def get(self, request, pk=None):
        if pk:
            # Consultar usuario por ID específico
            try:
                usuario = User.objects.get(pk=pk)
                usuario_data = {
                    "id": usuario.id,
                    "username": usuario.username,
                    "email": usuario.email,
                    "first_name": usuario.first_name,
                    "last_name": usuario.last_name,
                    "password":  request.data.get('password') 
                }
                return Response(usuario_data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Consultar todos los usuarios registrados
            usuarios = User.objects.all()
            usuarios_data = [
                {
                    "id": usuario.id,
                    "username": usuario.username,
                    "email": usuario.email,
                    "first_name": usuario.first_name,
                    "last_name": usuario.last_name,
                    "password":  request.data.get('password') 
                }
                for usuario in usuarios
            ]
            return Response(usuarios_data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        # Editar datos de un usuario específico, incluida la contraseña
        try:
            usuario = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Verificar si se ha incluido una contraseña para actualizarla
        if 'password' in request.data:
            password = request.data['password']
            password_confirm = request.data.get('password2', '')

            # Verificar que ambas contraseñas coincidan
            if password != password_confirm:
                return Response({"password": "Las contraseñas no coinciden."}, status=status.HTTP_400_BAD_REQUEST)

            # Validar la nueva contraseña
            try:
                validate_password(password, usuario)
            except serializers.ValidationError as e:
                return Response({"password": e.messages}, status=status.HTTP_400_BAD_REQUEST)

            # Actualizar la contraseña después de la validación
            usuario.set_password(password)

        # Serializar los demás campos
        serializer = RegistroSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario actualizado correctamente."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        # Eliminar un usuario específico
        try:
            usuario = User.objects.get(pk=pk)
            usuario.delete()
            return Response({"mensaje": "Usuario eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs): # llamar al método post de la clase padre para obtener el token
        response = super().post(request, *args, **kwargs)
        response.data['mensaje'] = "Autenticación satisfactoria."  # retornar la respuesta con el token y el mensaje
        return response

