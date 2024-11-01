from rest_framework import serializers
from .models import Cliente, TipoDocumento

# Serializador para TipoDocumento
class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ['id_tipo_docum', 'nom_tipo_doc']

# Serializador para Cliente
class ClienteSerializer(serializers.ModelSerializer):
    tipo_documento = serializers.PrimaryKeyRelatedField( queryset=TipoDocumento.objects.all(),source='id_tipo_docum')

    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nombre_cliente',
            'apellidos_cliente',
            'correo',
            'tipo_documento',
            'documento_cli',
            'telefono'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.id_tipo_docum:
            representation['tipo_documento'] = {
                "id": instance.id_tipo_docum.id_tipo_docum,
                "nombre": instance.id_tipo_docum.nom_tipo_doc
            }
        return representation