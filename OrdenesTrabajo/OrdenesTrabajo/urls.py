"""OrdenesTrabajo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from diagnosticos import views as diagnosticos_views
from dashboard import views as dashboard_views
from contactos import views as contactos_views
from vehiculos import views as vehiculos_views
from ordenes import views as ordenes_views

urlpatterns = [
    path('', dashboard_views.dashboard),
    # ejemplo de url con declaracion de variables y tipos
    # path('hi/<str:name>/<int:age>/', local_view),

    path('diagnosticos/', diagnosticos_views.main, name='diagnosticos'),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),

    path('contactos/', contactos_views.main, name='contactos'),
    path('crearContacto/', contactos_views.create, name='crear-contacto'),
    path('contacto/', contactos_views.contacto, name='detalle-contacto'),
    path('editContacto/', contactos_views.editContacto, name='edit-contacto'),
    path('eliminarContacto/', contactos_views.deleteContacto, name='eliminar-contacto'),

    path('vehiculos/', vehiculos_views.main, name='vehiculos'),
    path('crearVehiculo/', vehiculos_views.adminVehiculos, name='admin-vehiculos'),
    path('guardarVehiculo/', vehiculos_views.guardarVehiculo, name='guardar-vehiculo'),
    path('detalleVehiculo/', vehiculos_views.detalleVehiculo, name='detalles-vehiculo'),
    path('editarVehiculo/', vehiculos_views.editarVehiculo, name='editar-vehiculo'),
    path('eliminarVehiculo/', vehiculos_views.deleteVehiculo, name='eliminar-vehiculo'),

    path('ordenesTrabajo/', ordenes_views.listaOrdenes, name='ordenesTrabajo'),
    path('ordenesClientes/', ordenes_views.main, name='ordenes-clientes'),
    path('ordenVehiculos/', ordenes_views.ordenVehiculos, name='ordenes-vehiculos'),
    path('crearOrden/', ordenes_views.crearOrden, name='crear-orden'),
    path('guardarOrden/', ordenes_views.guardarOrden, name='guardar-orden'),
    path('detalleOrden/', ordenes_views.detalleOrden, name='detalle-orden'),
    path('editarOrden/', ordenes_views.editarOrden, name='editar-orden'),
    path('eliminarOrden/', ordenes_views.deleteOrden, name='eliminar-orden'),
]
