from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('banda', 'hora', 'precio', 'creado_por')
    list_filter = ('banda', 'hora')
    search_fields = ('banda__nombre',)
