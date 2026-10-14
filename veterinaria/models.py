
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    saldo = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Atencion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mascota = models.CharField(max_length=100)
    tipo_atencion = models.CharField(max_length=100)
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.mascota} - {self.tipo_atencion}"
