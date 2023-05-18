from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.index),
    path('About/', views.about),
    path('Saludar/', views.Saludar),
    path('Proyectos/', views.Proyectos, name='Proyectos'),
    path('Cuadros/', views.Cuadros),
    path('Equipos/', views.Equipos),
    path('Crear_form/', views.Crear_form),
    path('Crear_Proyecto/', views.Crear_Proyecto, name='Crear_Proyecto'),
    path('Crear_Liga/', views.Crear_Liga, name='Crear_Liga'),
    path('BusquedaLiga/', views.BusquedaLiga, name='BusquedaLiga'),
    path('buscar/', views.buscar, name='buscar'),
         ]
