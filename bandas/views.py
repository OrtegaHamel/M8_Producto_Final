from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
            messages.success(request, "Banda creada exitosamente.")
            return redirect('bandas:lista_bandas')
        else:
            # Mostrar errores del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
    else:
        form = BandaForm()

    return render(request, 'bandas/crear_banda.html', {'form': form})

@login_required
def editar_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            messages.success(request, "Banda actualizada exitosamente.")
            return redirect('bandas:lista_bandas')
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/editar_banda.html', {'form': form, 'banda': banda})

@login_required
def eliminar_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        banda.delete()
        messages.success(request, "Banda eliminada exitosamente.")
        return redirect('bandas:lista_bandas')
    return render(request, 'bandas/eliminar_banda.html', {'banda': banda})
