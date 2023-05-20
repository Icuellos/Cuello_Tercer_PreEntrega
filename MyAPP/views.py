
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Equipos, Liga
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearNuevoFormulario, CrearNuevoProyecto, CrearNuevaLiga, CrearNuevoEquipo, BuscarEquipoForm
# Create your views here.
def index(request):
    title = "Futbol infantil Uruguayo!!"
    return render(request, "Index.html", 
                  {'title': title})

def about(request):
    username = "icuello"
    return render(request, "About.html", {'username': username})


def Crear_form(request):
   # Proyectos = list(Proyecto.objects.values())
   #Equipos = equipos.objects.all()
   return render(request, 'Crear_form.html',
                 {'form': CrearNuevoFormulario})
   
def Proyectos(request):
   # Proyectos = list(Proyecto.objects.values())
   Ligas = Liga.objects.all()
   return render(request, 'Proyectos.html', {'Ligas': Ligas})   
   
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

#def Equipo(request):
    #equipos = Equipos.objects.all()
    #return render(request, 'Equipo.html', {'equipos': equipos}) 

def Crear_Equipo(request):
    if request.method == 'POST':
         form = CrearNuevoEquipo(request.POST)
         if form.is_valid():
            name = form.cleaned_data['name']
            equipo = Equipos(name=name)
            equipo.save()
            return redirect('Equipo')   
    else: 
        form = CrearNuevoEquipo()

    return render(request, 'Crear_Equipo.html', {'form': form})

def Equipo(request):
    equipos = Equipos.objects.all()
    return render(request, 'Equipo.html', {'equipos': equipos})    
 

def buscar_equipos(request):
    query = request.GET.get('query')
    equipos = None

    if query is not None:
        equipos = Equipos.objects.filter(name__icontains=query)

    return render(request, 'buscar_equipos.html', {'equipos': equipos, 'query': query})


        
def detalle_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    return render(request, 'detalle_equipo.html', {'equipo': equipo})  
  
#def detalle_equipo(request, equipo_id):
#    equipo = get_object_or_404(Equipos, id=equipo_id)
#    return render(request, 'detalle_equipo.html', {'equipo': equipo})    

#PARA ELIMINAR EQUIPOS
def eliminar_liga(request, liga_id):
    liga = Liga.objects.get(id=liga_id)
    liga.delete()
    return redirect('Proyectos')

#PARA ELIMINAR UNA LIGA
def eliminar_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    equipo.delete()
    return redirect('Equipo')




