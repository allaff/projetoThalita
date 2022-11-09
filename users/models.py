from django.db import models
from django.contrib.auth.models import User
from validation.validators import valida_cpf, valida_senha

class Users(models.Model):
  email = models.EmailField(max_length=256)
  senha = models.CharField(max_length=8, validators=[valida_senha], unique=True)
  cpf = models.IntegerField(validators=[valida_cpf], unique=True)
  funcaoEmpresa = models.BooleanField(default=True)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  def __str__(self) -> str:
    return self.nome
  