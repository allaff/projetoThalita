from dataclasses import fields

from django import forms

from .models import Users

funcaoNaEmpresa = (
  ('True', 'Funcionário', 'Recepsionista', 'Proprietário', 'Gerente', 'Contador'),
)
class UsersForm(forms.ModelForm):

  # email = forms.EmailField(max_length=256)
  # senha = forms.PasswordInput()
  # cpf = forms.IntegerField(max_length=11)
  funcaoEmpresa = forms.ChoiceField(choices=[funcaoNaEmpresa], required=True)

  class Meta:
    model = Users
    fields = ['email', 'senha', 'cpf', 'funcaoEmpresa']