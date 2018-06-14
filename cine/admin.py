from django.contrib import admin
from .models import Pelicula, Sala, Comentario, Visualizacion, Entrada

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Comentario)
admin.site.register(Visualizacion)
admin.site.register(Entrada)
