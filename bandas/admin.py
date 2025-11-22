from django.contrib import admin
from .models import Banda

@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'responsable', 'telefono', 'correo', 'redes_sociales')
    search_fields = ('nombre', 'responsable')
