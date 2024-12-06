# ======== AULA 02 ========
from django.urls import path
from livraria.views import home, sobre
from django.http import HttpResponse


urlpatterns = [
    path('', home, name='inicio'),
    path('sobre/', sobre, name='sobre')
]