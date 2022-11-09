from rest_framework import serializers
from users.models import Users

class UsuarioSerializer(serializers.ModelSerializer):
    #email = EmailSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = ['email', 'senha', 'cpf', 'funcaoEmpresa']
