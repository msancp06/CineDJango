from django.shortcuts import render
from django.utils.timezone import datetime
from .models import *
import json
from django.http import HttpResponse


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

    # Se define la fecha de hoy y se filtran las peliculas
    hoy = datetime.today()
    peliculasQueMostrar = Visualizacion.objects.filter(hora__gte = hoy)
    numeroDePeliculas = peliculasQueMostrar.count()
    arrayPeliculas = []
    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula in arrayPeliculas:
            arrayPeliculas.append(peliculasQueMostrar[x].pelicula)

    return render(request, 'cine/reservas.html', {'peliculas' : arrayPeliculas, 'visualizaciones' : peliculasQueMostrar})

def getSesionesAjax(request):

    idPelicula = request.GET.get('idPelicula', 1)
    sesiones_set = []
    todasLasSesiones = []

    print("idPelicula ", idPelicula)
    visualizacionesConPelicula = Visualizacion.objects.filter(pelicula = idPelicula)

    numeroDeSesiones = visualizacionesConPelicula.count()
    for x in range(0, numeroDeSesiones):
        print("horas: ", visualizacionesConPelicula[x].hora)
        todasLasSesiones.append(visualizacionesConPelicula[x])

    for sesion in todasLasSesiones:
        sesiones_set.append({'sesion': sesion.hora.strftime("%m/%d %H:%M"), 'idVisualizacion' : sesion.id, 'sala' : sesion.sala.id})

    return HttpResponse(json.dumps(sesiones_set), content_type='application/json')

def reservasPelicula(request, id_visualizacion):
    return render(request, 'cine/reservas')






def resumen(request):
    return render(request, 'cine/resumen.html')
