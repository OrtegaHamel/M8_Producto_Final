from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Banda
from .forms import BandaForm
from django.core.exceptions import PermissionDenied
from usuarios.decorators import grupo_required
from django.urls import reverse
from urllib.parse import urlencode

@login_required
def lista_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'bandas/lista_bandas.html', {'bandas': bandas})

@login_required
@grupo_required('Productores')
def crear_banda(request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('bandas:lista_bandas')}?mensaje=Banda+creada+exitosamente&tipo=success")
    else:
        form = BandaForm()

    return render(request, 'bandas/crear_banda.html', {'form': form})

@login_required
@grupo_required('Productores')
def editar_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('bandas:lista_bandas')}?mensaje=Banda+actualizada+exitosamente&tipo=success")
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/editar_banda.html', {'form': form, 'banda': banda})

@login_required
@grupo_required('Productores')
def eliminar_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        banda.delete()
        return redirect(f"{reverse('bandas:lista_bandas')}?mensaje=Banda+eliminada+exitosamente&tipo=success")
    return render(request, 'bandas/eliminar_banda.html', {'banda': banda})
