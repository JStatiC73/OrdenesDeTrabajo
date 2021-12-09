from django.http import HttpResponse
from django.shortcuts import render, redirect
from contactos.models import Contacto
from vehiculos.models import Vehiculo
from ordenes.models import EstadoOrden, Orden, TipoSolicitud

# Utilities
from datetime import datetime

def listaOrdenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'ordenes/ordenesTrabajo.html', { 'ordenes': ordenes })

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
    tiposSolicitud = TipoSolicitud.objects.all()
    cliente = Contacto.objects.get(pk=idCliente)
    vehiculo = Vehiculo.objects.get(pk=idVehiculo)
    return render(request, 'ordenes/createOrden.html', 
    { 
        'cliente': cliente, 
        'vehiculo': vehiculo,
        'estados': estados,
        'tiposSolicitud': tiposSolicitud
    })

def guardarOrden(request):
    if request.method == 'POST':
        idCliente = request.POST['idCliente']
        idVehiculo = request.POST['idVehiculo']
        idEstado = request.POST['estadoSolicitud']
        idTipoSolicitud = request.POST['tipoSolicitud']
        cliente = Contacto.objects.get(pk=idCliente)
        vehiculo = Vehiculo.objects.get(pk=idVehiculo)
        estado = EstadoOrden.objects.get(pk=idEstado)
        tipoSolicitud = TipoSolicitud.objects.get(pk=idTipoSolicitud)
        nuevaOrden = Orden()
        nuevaOrden.IdContacto = cliente
        nuevaOrden.IdVehiculo = vehiculo 
        nuevaOrden.DetalleSolicitud = request.POST['detalleSolicitud']
        nuevaOrden.IdEstado = estado
        nuevaOrden.TipoSolicitud = tipoSolicitud
        nuevaOrden.TipoReparacion = request.POST['tipoReparacion']

        nuevaOrden.Diagnostico = True if request.POST.get('diagnosticoCheck', False) == 'on' else False
        nuevaOrden.Repuesto = True if request.POST.get('compraRepuestoCheck', False) == 'on' else False
        nuevaOrden.RevisionFisica = True if request.POST.get('revisionFisicaCheck', False) == 'on' else False
        nuevaOrden.Intervencion = True if request.POST.get('intervencionCheck', False) == 'on' else False
        nuevaOrden.Scaner = True if request.POST.get('scanerCheck', False) == 'on' else False
        nuevaOrden.SolicitudRepuesto = True if request.POST.get('solicitudPresupuestoCheck', False) == 'on' else False
        
        nuevaOrden.save()

        return redirect('ordenesTrabajo')

def detalleOrden(request):
    idOrden = request.GET['idOrden']
    orden = Orden.objects.get(pk=idOrden)
    estados = EstadoOrden.objects.all()
    tiposSolicitud = TipoSolicitud.objects.all()
    return render(request, 'ordenes/detalleOrden.html', 
    { 
        'orden': orden,
        'estados': estados,
        'tiposSolicitud': tiposSolicitud
    })

def editarOrden(request):
    if request.method == 'POST':
        idOrden = request.POST['idOrden']
        orden = Orden.objects.get(pk=idOrden)
        idEstado = request.POST['estadoSolicitud']
        idTipoSolicitud = request.POST['tipoSolicitud']
        estado = EstadoOrden.objects.get(pk=idEstado)
        tipoSolicitud = TipoSolicitud.objects.get(pk=idTipoSolicitud)

        orden.DetalleSolicitud = request.POST['detalleSolicitud']
        orden.IdEstado = estado
        orden.TipoSolicitud = tipoSolicitud
        orden.TipoReparacion = request.POST['tipoReparacion']

        orden.Diagnostico = True if request.POST.get('diagnosticoCheck', False) == 'on' else False
        orden.Repuesto = True if request.POST.get('compraRepuestoCheck', False) == 'on' else False
        orden.RevisionFisica = True if request.POST.get('revisionFisicaCheck', False) == 'on' else False
        orden.Intervencion = True if request.POST.get('intervencionCheck', False) == 'on' else False
        orden.Scaner = True if request.POST.get('scanerCheck', False) == 'on' else False
        orden.SolicitudRepuesto = True if request.POST.get('solicitudPresupuestoCheck', False) == 'on' else False
        
        orden.save()

        return redirect('ordenesTrabajo')

def deleteOrden(request):
    idOrden = request.GET['idOrden']
    orden = Orden.objects.get(pk=idOrden)

    orden.delete()

    return redirect('ordenesTrabajo')