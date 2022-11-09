from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UsuarioSerializer

from users.models import Users


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('email')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuarios = super().get_queryset()
        usuarios = usuarios.filter(usuario=self.request.user)
        return usuarios
    