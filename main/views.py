from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from main.forms import NovoUserForm
from django.contrib.auth import login

class Home(TemplateView):
  template_name = 'main/index.html'

def register(request):

  if request.method == "POST":
    form = NovoUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, "Usuário cadastado com sucesso!")
      return redirect ('home')
    messages.error(request, "Erro ao cadastrar o usuário.")
  form = NovoUserForm()
  context = {'form': form}
  return render (request, template_name='main/register.html', context=context)
