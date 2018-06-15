from django.db import models

# Create your models here.

class Pelicula(models.Model):

    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=500)
    foto = models.ImageField()

    def __unicode___(self):
        return u'%s' % (self.titulo)

class Sala(models.Model):

    filas = models.IntegerField()
    asientosPorFila = models.IntegerField()
    asientosUltimaFila = models.IntegerField()

class Comentario(models.Model):

    tituloComentario = models.CharField(max_length=50)
    cuerpoComentario = models.CharField(max_length=250)
    pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)


class Visualizacion(models.Model):

    pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE)
    hora = models.DateTimeField()

    def __unicode___(self):
        return u'%s' % (self.hora)

class Entrada(models.Model):

    fila = models.IntegerField()
    asiento = models.IntegerField()
    visualizacion = models.ForeignKey(Visualizacion, on_delete = models.CASCADE)
