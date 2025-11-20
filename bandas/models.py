from django.db import models

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    redes_sociales = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
