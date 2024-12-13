from django.shortcuts import render, redirect
# ======== AULA 03 ========
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# ======== AULA 03 ========
def home(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro na autenticação, tente novamente')
            return redirect('home')

    else:
        return render(request, 'home.html')

def logout_user(request):
    pass