# Django 
from django.db import models


class Contacto(models.Model):
    IdContacto = models.BigAutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Telefono = models.CharField(max_length=13)
    Estado = models.BooleanField(default=True)

    def NombreCompleto(self):
        return self.Nombre + ' ' + self.Apellido

    def EstadoStr(self):
        return 'Activo' if self.Estado else 'Inactivo'