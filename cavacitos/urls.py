from django.urls import path
from django.conf.urls import url
from .views import *
from django.conf.urls import include

urlpatterns = [
    path('', home, name='index'),
    path('cobro/', cobro, name='cobro'),
    path('login/', login, name='login'),
    path('login/agrega/', agrega, name='login/agrega'),
    path('login/edita/', edita, name='login/edita'),

]
