from django.http import HttpResponse
from django.shortcuts import render, redirect
from contactos.models import Contacto


# Utilities
from datetime import datetime

# Create your views here.
def main(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/createContacto.html', { 'contactos': contactos })

def create(request):
    if request.method == 'POST':
        nuevoContacto = Contacto()
        nuevoContacto.Nombre = request.POST['nombreContacto']
        nuevoContacto.Apellido = request.POST['apellidoContacto']
        nuevoContacto.Email = request.POST['emailContacto']
        nuevoContacto.Telefono = request.POST['telefonoContacto']
    
        nuevoContacto.save()

        return redirect('contactos')

    return render(request, 'contactos/createContacto.html')

def contacto(request):
    idContacto = request.GET['idContacto']
    contacto = Contacto.objects.get(pk = idContacto)

    return render(request, 'contactos/editContacto.html', { 'contacto' : contacto })

def editContacto(request):
    idContacto = request.POST['idContacto']
    contacto = Contacto.objects.get(pk = idContacto)
    contacto.Nombre = request.POST['nombreContacto']
    contacto.Apellido = request.POST['apellidoContacto']
    contacto.Email = request.POST['emailContacto']
    contacto.Telefono = request.POST['telefonoContacto']

    contacto.save()

    return redirect('contactos')

def deleteContacto(request):
    idContacto = request.GET['idContacto']
    contacto = Contacto.objects.get(pk = idContacto)
    contacto.Estado = False
    contacto.save()

    return redirect('contactos')