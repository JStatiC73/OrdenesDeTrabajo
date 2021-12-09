from django.contrib import admin
from ordenes.models import Orden, EstadoOrden, TipoSolicitud

# Register your models here.
admin.site.register(EstadoOrden)
admin.site.register(TipoSolicitud)
admin.site.register(Orden)