from django.shortcuts import render
from django.utils.timezone import datetime
from .models import *
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from cine.forms import CineForm

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

def indexGenero(request, genero):

    # Se define la fecha de hoy y se filtran las peliculas
    hoy = datetime.today()
    peliculasQueMostrar = Visualizacion.objects.filter(hora__gte = hoy)
    numeroDePeliculas = peliculasQueMostrar.count()
    arrayPeliculas = []
    arrayGeneros = []
    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula in arrayPeliculas:
            if peliculasQueMostrar[x].pelicula.genero == genero:
                arrayPeliculas.append(peliculasQueMostrar[x].pelicula)

    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula.genero in arrayGeneros:
            arrayGeneros.append(peliculasQueMostrar[x].pelicula.genero)

    return render(request, 'cine/index.html', {'peliculas' : arrayPeliculas, 'generos' : arrayGeneros})


def detalles(request, id_pelicula):

    pelicula = Pelicula.objects.get(id = id_pelicula)
    visualizacionesConPelicula = Visualizacion.objects.filter(pelicula = id_pelicula)
    comentarios = Comentario.objects.filter(pelicula = pelicula).all()

    if request.method == 'POST':
        form = CineForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            comentario = form.cleaned_data['comentario']

            nuevoComentario = Comentario(tituloComentario = titulo, cuerpoComentario = comentario, pelicula = pelicula)
            nuevoComentario.save()

            request.method = 'GET'
            return detalles(request, id_pelicula)
    else:
        form = CineForm()

    return render(request, 'cine/detalles.html', {'pelicula' : pelicula, 'sesiones' : visualizacionesConPelicula, 'comentarios' : comentarios, 'form' : form})

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

def getSalasAjax(request):

    idSala = request.GET.get('idSala', 1)
    sala = Sala.objects.get(id = idSala)
    sala_set = []

    sala_set.append({'idSala' : sala.id , 'filas' : sala.filas, 'asientosPorFila' : sala.asientosPorFila, 'asientosUltimaFila' : sala.asientosUltimaFila})
    print("salaFilas: ", sala.filas)
    return HttpResponse(json.dumps(sala_set), content_type='application/json')




def reservasPelicula(request, id_visualizacion):
    return render(request, 'cine/reservas')






def resumen(request):
    return render(request, 'cine/resumen.html')
