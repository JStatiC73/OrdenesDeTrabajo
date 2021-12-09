from django.contrib import admin
from ordenes.models import Orden, EstadoOrden

# Register your models here.
admin.site.register(EstadoOrden)
admin.site.register(Orden)