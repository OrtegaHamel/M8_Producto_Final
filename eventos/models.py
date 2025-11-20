from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    banda = models.ForeignKey('bandas.Banda', on_delete=models.CASCADE)
    hora = models.DateTimeField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.banda.nombre} - {self.hora}"

