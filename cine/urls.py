from django.urls import path
from . import views

app_name = 'cine'
urlpatterns = [
    path('inicio', views.index, name='index'),
    path('inicio/<str:genero>', views.indexGenero, name='index_genero'),
    path('detalles/<int:id_pelicula>', views.detalles, name='detalles'),
    path('reservas', views.reservas, name='reservas'),
    path('resumen', views.resumen, name='resumen'),
    path('getSesionesAjax/', views.getSesionesAjax, name='getSesionesAjax'),
    path('getSalasAjax/', views.getSalasAjax, name='getSalasAjax'),
    path('getEntradasAjax/', views.getEntradasAjax, name='getEntradasAjax'),
    path('saveEntradasAjax/', views.saveEntradasAjax, name='saveEntradasAjax'),
]
