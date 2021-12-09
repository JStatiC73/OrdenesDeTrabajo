from django.db import models

class EstadoOrden(models.Model):
    IdEstado = models.SmallAutoField(primary_key=True)
    Descripcion = models.CharField(max_length=60)

class Orden(models.Model):
    IdOrden = models.BigAutoField(primary_key=True)
    IdContacto = models.ForeignKey('contactos.Contacto', on_delete=models.CASCADE)
    IdVehiculo = models.ForeignKey('vehiculos.Vehiculo', on_delete=models.CASCADE)
    DetalleSolicitud = models.CharField(max_length=200)
    IdEstado = models.ForeignKey('EstadoOrden', on_delete=models.CASCADE)
    TipoSolicitud = models.CharField(max_length=200)
    TipoReparacion = models.CharField(max_length=200)
    Diagnostico = models.BooleanField(default=False)
    Repuesto = models.BooleanField(default=False)
    RevisionFisica = models.BooleanField(default=False)
    Intervencion = models.BooleanField(default=False)
    Scaner = models.BooleanField(default=False)
    SolicitudRepuesto = models.BooleanField(default=False)