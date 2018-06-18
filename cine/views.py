from django.shortcuts import render
from django.utils.timezone import datetime
from .models import *
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from cine.forms import CineForm
from django.shortcuts import redirect

# Create your views here.

def index(request):

    # Se define la fecha de hoy y se filtran las peliculas
    hoy = datetime.today()
    peliculasQueMostrar = Visualizacion.objects.filter(hora__gte = hoy)
    numeroDePeliculas = peliculasQueMostrar.count()
    arrayPeliculas = []
    arrayGeneros = []

    if request.method == 'POST':
        if request.POST.get('buscar'):
            # Si se ha enviado alguna palabra para burcar, devolvemos la vista generada
            # a partir de la busqueda
            return indexBusqueda(request, request.POST.get('buscar'));
    # Se cargan todas las peliculas y generos
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
        # Se aniaden solo las peliculas con el mismo genero
        if not peliculasQueMostrar[x].pelicula in arrayPeliculas:
            if peliculasQueMostrar[x].pelicula.genero == genero:
                arrayPeliculas.append(peliculasQueMostrar[x].pelicula)

    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula.genero in arrayGeneros:
            arrayGeneros.append(peliculasQueMostrar[x].pelicula.genero)

    return render(request, 'cine/index.html', {'peliculas' : arrayPeliculas, 'generos' : arrayGeneros, 'generoDePeli' : genero})


def indexBusqueda(request, buscar):

    # Se define la fecha de hoy y se filtran las peliculas
    hoy = datetime.today()
    peliculasQueMostrar = Visualizacion.objects.filter(hora__gte = hoy)
    numeroDePeliculas = peliculasQueMostrar.count()
    arrayPeliculas = []
    arrayGeneros = []
    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula in arrayPeliculas:
            # Se aniaden solo las peliculas que contengan parte del titulo
            if buscar.lower() in peliculasQueMostrar[x].pelicula.titulo.lower():
                arrayPeliculas.append(peliculasQueMostrar[x].pelicula)
            # o las peliculas que contengan parte del director
            elif buscar.lower() in peliculasQueMostrar[x].pelicula.director.lower():
                arrayPeliculas.append(peliculasQueMostrar[x].pelicula)
    for x in range(0, numeroDePeliculas):
        if not peliculasQueMostrar[x].pelicula.genero in arrayGeneros:
            arrayGeneros.append(peliculasQueMostrar[x].pelicula.genero)

    return render(request, 'cine/index.html', {'peliculas' : arrayPeliculas, 'generos' : arrayGeneros})


def detalles(request, id_pelicula):

    hoy = datetime.today()
    pelicula = Pelicula.objects.get(id = id_pelicula)
    visualizacionesConPelicula = Visualizacion.objects.filter(pelicula = id_pelicula).filter(hora__gte = hoy)
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
    visualizacionesQueMostrar = Visualizacion.objects.filter(hora__gte = hoy)
    numeroDePeliculas = visualizacionesQueMostrar.count()
    arrayPeliculas = []
    for x in range(0, numeroDePeliculas):
        if not visualizacionesQueMostrar[x].pelicula in arrayPeliculas:
            arrayPeliculas.append(visualizacionesQueMostrar[x].pelicula)

    return render(request, 'cine/reservas.html', {'peliculas' : arrayPeliculas, 'visualizaciones' : visualizacionesQueMostrar})


def getSesionesAjax(request):

    idPelicula = request.GET.get('idPelicula', 1)
    sesiones_set = []
    todasLasSesiones = []

    visualizacionesConPelicula = Visualizacion.objects.filter(pelicula = idPelicula)

    numeroDeSesiones = visualizacionesConPelicula.count()
    for x in range(0, numeroDeSesiones):
        todasLasSesiones.append(visualizacionesConPelicula[x])

    for sesion in todasLasSesiones:
        sesiones_set.append({'sesion': sesion.hora.strftime("%m/%d %H:%M"), 'idVisualizacion' : sesion.id, 'sala' : sesion.sala.id})

    return HttpResponse(json.dumps(sesiones_set), content_type='application/json')


def getSalasAjax(request):

    idSala = request.GET.get('idSala', 1)
    sala = Sala.objects.get(id = idSala)
    sala_set = []

    sala_set.append({'idSala' : sala.id , 'filas' : sala.filas, 'asientosPorFila' : sala.asientosPorFila, 'asientosUltimaFila' : sala.asientosUltimaFila})

    return HttpResponse(json.dumps(sala_set), content_type='application/json')

def getEntradasAjax(request):
    idVisualizacion = request.GET.get('idVisualizacion', 1)
    visualizacion = Visualizacion.objects.filter(id = idVisualizacion).get()
    entrada_set = visualizacion.entrada_set.all()
    entradas = []
    for entrada in entrada_set:
        entradas.append({'fila' : entrada.fila, 'asiento' : entrada.asiento})

    return HttpResponse(json.dumps(entradas), content_type='application/json')


def saveEntradasAjax(request):
    entradas = request.GET.getlist('arrayEntradas[]')

    for entrada in entradas:
        # Preparamos las variables para la entrada
        repEntrada = entrada.split(".")
        idSesion = repEntrada[0]
        fila = repEntrada[1]
        asiento = repEntrada[2]

        visualizacion = Visualizacion.objects.filter(id = idSesion).get()
        nuevaEntrada = Entrada(fila = fila, asiento = asiento, visualizacion = visualizacion)
        nuevaEntrada.save()

    return redirect('../reservas')


def reservasPelicula(request, id_visualizacion):
    return render(request, 'cine/reservas')



def resumen(request):
    if request.method == 'POST':
        entradasReservadas = []
        checkBoxes = request.POST.getlist('checks[]')

        for entrada in checkBoxes:
            print('entrada:' ,entrada)
            # Preparamos las variables para la entrada
            repEntrada = entrada.split(",")
            idSesion = repEntrada[0]
            fila = repEntrada[1]
            asiento = repEntrada[2]

            visualizacion = Visualizacion.objects.filter(id = idSesion).get()
            nuevaEntrada = Entrada(fila = fila, asiento = asiento, visualizacion = visualizacion)
            nuevaEntrada.save()
            entradasReservadas.append(nuevaEntrada)

    return render(request, 'cine/resumen.html', {'entradas' : entradasReservadas})
