from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Evento
from bandas.models import Banda 
from .forms import EventoForm

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all().order_by('hora')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def crear_evento(request):
    if not Banda.objects.exists():
        messages.warning(request, "No hay bandas creadas. Por favor, crea una banda primero.")
        return redirect('bandas:crear_banda')

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creado_por = request.user
            evento.save()
            messages.success(request, "Evento creado exitosamente.")
            return redirect('eventos:lista_eventos')
    else:
        form = EventoForm()

    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento actualizado exitosamente.")
            return redirect('eventos:lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento eliminado exitosamente.")
        return redirect('eventos:lista_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

