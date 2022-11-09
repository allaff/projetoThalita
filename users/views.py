from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from .forms import UsersForm
from .models import Users


class ListUsersView(ListView):
    model = Users
    queryset = Users.objects.all().order_by('email')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        filtro_email = self.request.GET.get('email') or None

        if (filtro_email):
            queryset = queryset.filter(email__contains=filtro_email)
        return queryset


class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm
    success_url = '/usuarios/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UsersForm
    success_url = '/usuarios/'


class UsersDeleteView(DeleteView):
    model = Users
    success_url = '/usuarios/'
