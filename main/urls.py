from django.urls import path
from .views import Home, register
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Home.as_view()), name='home'),
    path('accounts/register', register, name='register'),
]
