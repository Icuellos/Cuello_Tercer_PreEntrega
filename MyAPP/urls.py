from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.index),
    path('About/', views.about),
    path('Proyectos/', views.Proyectos, name='Proyectos'),
    path('Crear_form/', views.Crear_form, name='form'),
    path('Crear_Proyecto/', views.Crear_Proyecto, name='Crear_Proyecto'),
    path('Crear_Liga/', views.Crear_Liga, name='Crear_Liga'),
    path('BusquedaLiga/', views.BusquedaLiga, name='BusquedaLiga'),
    path('buscar/', views.buscar, name='buscar'),
    path('buscar/', views.buscar, name='buscar'),
    path('Equipo/', views.Equipo, name='Equipo'),
    path('Crear_Equipo/', views.Crear_Equipo, name='Crear_Equipo'),
         ]
