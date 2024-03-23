from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('index/signup', views.signup, name='signup'),
    path('index/login', views.login, name='login'),
]