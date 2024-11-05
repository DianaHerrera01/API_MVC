from django.contrib.auth.models import User # importar el modelo de usuario predeterminado de Django
from rest_framework import serializers
from rest_framework.validators import UniqueValidator  # importar validador para verificar la unicidad de un campo
from django.contrib.auth.password_validation import validate_password  # importar validador de contraseña de Django para aplicar políticas de seguridad
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # importar el serializador de token JWT de DRF-SimpleJWT

class RegistroSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],  # Verificar unicidad del username
        error_messages={
            'required': 'El nombre de usuario es obligatorio.',
            'unique': 'Este nombre de usuario ya está en uso.'
        }
    )
    email = serializers.EmailField(
        required=True,
        error_messages={
            'required': 'El correo electrónico es obligatorio.'
        }
    )
    password = serializers.CharField(
        required=True,  
        validators=[validate_password],
        error_messages={
            'required': 'La contraseña es obligatoria.'
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            'required': 'La confirmación de contraseña es obligatoria.'
        }
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        # Validar que las contraseñas coincidan
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
            
        return attrs

    def create(self, validated_data):
        # Remover el campo password2 ya que no es necesario para la creación
        validated_data.pop('password2')
        
        # Crear el usuario
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        # Actualizar los campos del usuario
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Si hay una nueva contraseña, establecerla
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # obtener el token utilizando la implementación de la clase padre
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Validar las credenciales y obtener los token
        return {
            "access": data.get("access"),
            "mensaje": "Autenticación satisfactoria."
        }