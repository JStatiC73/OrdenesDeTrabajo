from django.http import HttpResponse
from django.shortcuts import render, redirect
from contactos.models import Contacto
from vehiculos.models import Vehiculo


# Utilities
from datetime import datetime

# Create your views here.
def main(request):
    contactos = Contacto.objects.all()
    return render(request, 'vehiculos/clientes.html', { 'contactos': contactos })

def adminVehiculos(request):
    idCliente = request.GET['idCliente']
    cliente = Contacto.objects.get(pk = idCliente)
    return render(request, 'vehiculos/createVehiculo.html', { 'cliente': cliente })

def guardarVehiculo(request):
    if request.method == 'POST':
        nuevoVehiculo = Vehiculo()
        nuevoVehiculo.IdContacto = request.POST['idCliente']
        nuevoVehiculo.Serie = request.POST['serieVehiculo']
        nuevoVehiculo.Year = request.POST['yearVehiculo']
        nuevoVehiculo.Color = request.POST['colorVehiculo']
        nuevoVehiculo.Marca = request.POST['marcaVehiculo']
        nuevoVehiculo.Linea = request.POST['lineaVehiculo']
    
        nuevoVehiculo.save()

        return redirect('crearVehiculo/?idCliente=' + str(nuevoVehiculo.IdContacto))

    contactos = Contacto.objects.all()
    return render(request, 'vehiculos/clientes.html', { 'contactos': contactos })