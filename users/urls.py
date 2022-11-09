from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import UsersCreateView, UsersUpdateView, UsersDeleteView, ListUsersView
from . import views

urlpatterns = [
    path('', login_required(ListUsersView.as_view()), name='users.index'),
    path('novo/', login_required(UsersCreateView.as_view()), name='users.novo'),
    path('editar/<int:pk>/editar', login_required(UsersUpdateView.as_view()), name='users.editar'),
    path('excluir/<int:pk>/excluir', login_required(UsersDeleteView.as_view()), name='users.excluir'),
]
