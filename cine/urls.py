from django.urls import path
from . import views

app_name = 'cine'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:genero>', views.indexGenero, name='index_genero'),
    path('detalles/<int:id_pelicula>', views.detalles, name='detalles'),
    path('reservas', views.reservas, name='reservas'),
    path('reservas/<int:id_visualizacion>', views.reservasPelicula, name='reservas_pelicula'),
    path('resumen', views.resumen, name='resumen'),
    path('getSesionesAjax/', views.getSesionesAjax, name='getSesionesAjax'),
    path('getSalasAjax/', views.getSalasAjax, name='getSalasAjax'),
]
