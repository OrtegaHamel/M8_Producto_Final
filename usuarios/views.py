from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def user_login(request):
    if request.GET.get('next'):
        messages.warning(request, "Debes iniciar sesión para acceder a esa página.")

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next') or 'eventos:lista_eventos'
            return redirect(next_url)
        else:
            messages.error(request, "Usuario o contraseña inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('usuarios:login')