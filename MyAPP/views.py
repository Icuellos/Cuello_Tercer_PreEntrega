
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Equipos, Liga
from django.shortcuts import render, redirect
from .forms import CrearNuevoFormulario, CrearNuevoProyecto, CrearNuevaLiga
# Create your views here.
def index(request):
    title = "Futbol infantil Uruguayo!!"
    return render(request, "Index.html", 
                  {'title': title})

def about(request):
    username = "icuello"
    return render(request, "About.html", {'username': username})


def Proyectos(request):
   # Proyectos = list(Proyecto.objects.values())
   Ligas = Liga.objects.all()
   return render(request, 'Proyectos.html', {'Ligas': Ligas})

def Crear_form(request):
   # Proyectos = list(Proyecto.objects.values())
   #Equipos = equipos.objects.all()
   return render(request, 'Crear_form.html',
                 {'form': CrearNuevoFormulario})
   
def Crear_Proyecto(request):
    if request.method == 'GET':
     return render(request, 'Crear_Proyecto.html', 
                  {'form': CrearNuevoProyecto()
    })
    else:
        print (request.POST)
        Proyectos = Proyecto.objects.create(name=request.POST["name"])
        return render(request, 'Crear_Proyecto.html', 
                  {'form': CrearNuevoProyecto()
    })
        
def Crear_Liga(request):
    if request.method == 'POST':
        form = CrearNuevaLiga(request.POST)
        if form.is_valid():
            liga = Liga()  
            liga.name = form.cleaned_data['name']  #
            liga.save()  

            return redirect('Proyectos')  
    else:
        form = CrearNuevaLiga()  

    return render(request, 'Crear_Liga.html', {'form': form})

    
def BusquedaLiga(request):
    return render(request, 'MyAPP/Busqueda_Liga.html')   

def buscar(request):
    respuesta = f"Estoy buscando la liga número: {Liga}"
   
    return HttpResponse(respuesta)


