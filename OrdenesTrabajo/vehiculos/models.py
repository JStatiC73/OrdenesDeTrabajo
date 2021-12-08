from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    IdVehiculo = models.BigAutoField(primary_key=True)
    IdContacto = models.ForeignKey('contactos.Contacto', on_delete=models.CASCADE)
    Serie = models.CharField(max_length=100)
    Year = models.IntegerField()
    Color = models.CharField(max_length=60)
    Marca = models.CharField(max_length=100)
    Linea = models.CharField(max_length=100)