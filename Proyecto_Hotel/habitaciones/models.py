from django.db import models

# Create your models here.


class Habitacion(models.Model):
    numero = models.IntegerField(unique=True, verbose_name="Número de Habitación")
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Habitación")
    precio = models.IntegerField(verbose_name="Precio por Noche")
    disponible = models.BooleanField(default=True, verbose_name="¿Está Disponible?")

    def __str__(self):
        return f"Habitación {self.numero}"