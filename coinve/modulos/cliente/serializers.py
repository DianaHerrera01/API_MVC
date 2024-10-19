from rest_framework import serializers
from .models import Cliente, TipoDocumento

# Serializador para TipoDocumento
class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ['nom_tipo_doc']

# Serializador para Cliente
class ClienteSerializer(serializers.ModelSerializer):
    id_tipo_docum = serializers.PrimaryKeyRelatedField(queryset=TipoDocumento.objects.all())

    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nombre_cliente',
            'apellidos_cliente',
            'correo',
            'id_tipo_docum',
            'documento_cli',
            'telefono'
        ]