from django.shortcuts import render
from django.utils.timezone import datetime
from .models import Visualizacion


# Create your views here.

def index(request):

    # Se define la fecha de hoy y se filtran las peliculas
    hoy = datetime.today()
    peliculasQueMostrar = Visualizacion.objects.filter(hora__gte = hoy)
    numeroDePeliculas = peliculasQueMostrar.count()
    arrayPeliculas = []
    arrayGeneros = []
    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula in arrayPeliculas:
            arrayPeliculas.append(peliculasQueMostrar[x].pelicula)

    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula.genero in arrayGeneros:
            arrayGeneros.append(peliculasQueMostrar[x].pelicula.genero)

    return render(request, 'cine/index.html', {'peliculas' : arrayPeliculas, 'generos' : arrayGeneros})

def detalles(request):
    return render(request, 'cine/detalles.html')

def reservas(request):
    return render(request, 'cine/reservas.html')

def reservasPelicula(request, id_visualizacion):
    return render(request, 'cine/reservas')

def resumen(request):
    return render(request, 'cine/resumen.html')
