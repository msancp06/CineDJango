from django.urls import path
from . import views

app_name = 'cine'
urlpatterns = [
    path('', views.index, name='index'),
    path('detalles/<int:id_pelicula>', views.detalles, name='detalles'),
    path('reservas', views.reservas, name='reservas'),
    path('reservas/<int:id_visualizacion>', views.reservasPelicula, name='reservas_pelicula'),
    path('resumen', views.resumen, name='resumen'),
]