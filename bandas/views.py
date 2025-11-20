from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Banda
from .forms import BandaForm

@login_required
def lista_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'bandas/lista_bandas.html', {'bandas': bandas})

@login_required
def crear_banda(request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_bandas')
    else:
        form = BandaForm()
    return render(request, 'bandas/crear_banda.html', {'form': form})
