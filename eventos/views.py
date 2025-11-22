from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Evento
from bandas.models import Banda 
from .forms import EventoForm, BusquedaEventosForm
from django.core.exceptions import PermissionDenied
from usuarios.decorators import grupo_required
from django.urls import reverse
from urllib.parse import urlencode
from django.utils import timezone
from datetime import timedelta, datetime

def home_publico(request):
    today = timezone.now()

    # Eventos del mes actual
    eventos_mes_actual = Evento.objects.filter(
        hora__month=today.month,
        hora__year=today.year
    ).order_by('hora')

    # Eventos futuros (meses futuros)
    eventos_futuros = Evento.objects.filter(
        hora__gt=timezone.now()
    ).exclude(
        hora__month=today.month,
        hora__year=today.year
    ).order_by('hora')

    return render(request, 'home_publico.html', {
        'eventos_mes_actual': eventos_mes_actual,
        'eventos_futuros': eventos_futuros,
    })


@login_required
def lista_eventos(request):
    eventos = Evento.objects.all().order_by('hora')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
@grupo_required('Productores')
def crear_evento(request):
    if not Banda.objects.exists():
        return redirect(f"{reverse('bandas:crear_banda')}?mensaje=No+hay+bandas+creadas.+Crea+una+banda+primero.&tipo=warning")

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creado_por = request.user
            evento.save()
            return redirect(f"{reverse('eventos:lista_eventos')}?mensaje=Evento+creado+exitosamente&tipo=success")
    else:
        form = EventoForm()

    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
@grupo_required('Productores')
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('eventos:lista_eventos')}?mensaje=Evento+actualizado+exitosamente&tipo=success")
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

@login_required
@grupo_required('Productores')
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect(f"{reverse('eventos:lista_eventos')}?mensaje=Evento+eliminado+exitosamente&tipo=success")
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})


def busqueda_eventos(request):
    form = BusquedaEventosForm(request.GET or None)
    eventos = Evento.objects.all().order_by('hora')
    bandas_conteos = None
    banda_seleccionada = None

    if form.is_valid():
        banda = form.cleaned_data.get('banda')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')

        if banda:
            banda_seleccionada = banda
            eventos = eventos.filter(banda=banda)
            bandas_conteos = Evento.objects.filter(banda=banda).aggregate(
                conteo=Count('id')
            )

        if fecha_inicio:
            eventos = eventos.filter(hora__date__gte=fecha_inicio)
        if fecha_fin:
            eventos = eventos.filter(hora__date__lte=fecha_fin)

    return render(request, 'eventos/busqueda_eventos.html', {
        'form': form,
        'eventos': eventos,
        'bandas_conteos': bandas_conteos,
        'banda_seleccionada': banda_seleccionada,
    })
