from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    fecha = models.DateTimeField()
    numero_comensales = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"