from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.index),
    path('About/', views.about),
    path('Proyectos/', views.Proyectos, name='Proyectos'),
    path('Crear_form/', views.Crear_form, name='form'),
    path('Crear_Proyecto/', views.Crear_Proyecto, name='Crear_Proyecto'),
    path('Crear_Liga/', views.Crear_Liga, name='Crear_Liga'),
    path('buscar_equipos/', views.buscar_equipos, name='buscar_equipos'),
    path('Equipo/', views.Equipo, name='Equipo'),
    path('Crear_Equipo/', views.Crear_Equipo, name='Crear_Equipo'),
    path('equipo/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
         ]
