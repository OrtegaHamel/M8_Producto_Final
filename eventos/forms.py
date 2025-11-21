from django import forms
from django.forms import ModelChoiceField, DateTimeInput
from .models import Evento
from bandas.models import Banda
class EventoForm(forms.ModelForm):
    banda = ModelChoiceField(
        queryset=Banda.objects.all(),
        empty_label="Seleccione una banda",
        required=True,
    )

    class Meta:
        model = Evento
        fields = ['banda', 'hora', 'precio', 'descripcion']
        widgets = {
            'hora': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['banda'].help_text = (
            'Si la banda no está en la lista, '
            '<a href="/bandas/crear/" target="_blank">crea una nueva banda aquí</a>.'
        )
