from django.shortcuts import render
# ======== AULA 02 ========
from django.http import HttpResponse

# Create your views here.

# ======== AULA 02 ========
def home(request):
    return render(request, 'home.html',)

def sobre(request):
    return render(request, 'sobre.html',)