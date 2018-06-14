from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cine/index.html')

def detalles(request):
    return render(request, 'cine/detalles.html')

def reservas(request):
    return render(request, 'cine/reservas.html')

def reservasPeliculas(request, id_visualizacion):
    return render(request, 'cine/reservas')

def resumen(request):
    return render(request, 'cine/resumen.html')
