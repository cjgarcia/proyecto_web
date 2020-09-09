from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length = 50, help_text='Agrede su nombre')
    apellido = models.CharField(max_length = 50, help_text='Agrede su Apellido')
    fecha = models.DateTimeField()
    numero_comensales = models.IntegerField(max_length = 50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"