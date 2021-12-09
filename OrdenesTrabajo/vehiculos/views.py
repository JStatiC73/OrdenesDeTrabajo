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
    vehiculos = Vehiculo.objects.filter(IdContacto = cliente)
    return render(request, 'vehiculos/createVehiculo.html', { 'cliente': cliente, 'vehiculos': vehiculos })

def guardarVehiculo(request):
    if request.method == 'POST':
        nuevoVehiculo = Vehiculo()
        idContacto = request.POST['idCliente']
        contacto = Contacto.objects.get(pk = idContacto)
        nuevoVehiculo.IdContacto = contacto
        nuevoVehiculo.Serie = request.POST['serieVehiculo']
        nuevoVehiculo.Year = request.POST['yearVehiculo']
        nuevoVehiculo.Color = request.POST['colorVehiculo']
        nuevoVehiculo.Marca = request.POST['marcaVehiculo']
        nuevoVehiculo.Linea = request.POST['lineaVehiculo']
    
        nuevoVehiculo.save()

        return redirect('/crearVehiculo/?idCliente=' + str(idContacto))

    contactos = Contacto.objects.all()
    return render(request, 'vehiculos/clientes.html', { 'contactos': contactos })

def deleteVehiculo(request):
    idVehiculo = request.GET['idVehiculo']
    vehiculo = Vehiculo.objects.get(pk = idVehiculo)
    vehiculo.delete()

    return redirect('/crearVehiculo/?idCliente=' + str(vehiculo.IdContacto.IdContacto))

def detalleVehiculo(request):
    idVehiculo = request.GET['idVehiculo']
    vehiculo = Vehiculo.objects.get(pk = idVehiculo)

    return render(request, 'vehiculos/editarVehiculo.html', { 'vehiculo': vehiculo })

def editarVehiculo(request):
    if request.method == 'POST':
        idVehiculo = request.POST['idVehiculo']
        vehiculo = Vehiculo.objects.get(pk = idVehiculo)
        vehiculo.Serie = request.POST['serieVehiculo']
        vehiculo.Year = request.POST['yearVehiculo']
        vehiculo.Color = request.POST['colorVehiculo']
        vehiculo.Marca = request.POST['marcaVehiculo']
        vehiculo.Linea = request.POST['lineaVehiculo']
    
        vehiculo.save()

        return redirect('/crearVehiculo/?idCliente=' + str(vehiculo.IdContacto.IdContacto))
