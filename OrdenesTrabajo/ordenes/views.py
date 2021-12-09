from django.http import HttpResponse
from django.shortcuts import render
from contactos.models import Contacto
from vehiculos.models import Vehiculo
from ordenes.models import EstadoOrden, Orden

# Utilities
from datetime import datetime

# Create your views here.
def main(request):
    contactos = Contacto.objects.filter(Estado=True)
    return render(request, 'ordenes/ordenClientes.html', { 'contactos': contactos })

def ordenVehiculos(request):
    idCliente = request.GET['idCliente']
    cliente = Contacto.objects.get(pk=idCliente)
    vehiculos = Vehiculo.objects.filter(IdContacto=cliente)
    return render(request, 'ordenes/ordenVehiculos.html', { 'vehiculos': vehiculos })

def crearOrden(request):
    idCliente = request.GET['idCliente']
    idVehiculo = request.GET['idVehiculo']

    estados = EstadoOrden.objects.all()
    cliente = Contacto.objects.get(pk=idCliente)
    vehiculo = Vehiculo.objects.get(pk=idVehiculo)
    return render(request, 'ordenes/createOrden.html', 
    { 
        'cliente': cliente, 
        'vehiculo': vehiculo,
        'estados': estados,
    })