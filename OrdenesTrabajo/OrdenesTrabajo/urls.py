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

    path('diagnosticos/', diagnosticos_views.main),
    path('dashboard/', dashboard_views.dashboard),
    path('contactos/', contactos_views.main),
    path('vehiculos/', vehiculos_views.main),
    path('ordenes/', ordenes_views.main),
]
