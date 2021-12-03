from django.http import HttpResponse
from django.shortcuts import render


# Utilities
from datetime import datetime

# Create your views here.
def main(request):
    return render(request, 'diagnosticos/createDiagnostico.html')