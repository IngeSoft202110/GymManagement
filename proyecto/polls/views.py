from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .models import Usuario,Rutina, Ejercicio, EjercicioXRutina
from django.db.models import Q

@csrf_exempt
def loginView(request):
    return render(request, 'login.html')

def guardarRutinaView(request):
    return render(request, 'guardarRutina.html')

def guardarejerciciosView(request): 
    return render(request, 'guardarejercicios.html')

def index(request):
    return render(request, 'index.html')


def mainView(request):
    return render(request, 'main_view.html')


def registerView(request):
    return render(request, 'register.html')
    
def exerciseView(request):
    ejercicios = Ejercicio.objects.all()
    return render(request, 'exercise.html',{'ejercicios':ejercicios})

def exercisesListView(request):
    return render(request, 'exercisesList.html')

def register(request):

    if request.method == 'POST':
        usuario = request.POST['user']
        nombres = request.POST['nombre']
        apellidos = request.POST['apellido']
        correo = request.POST['email']
        genero = request.POST['genero']
        fecha_nacimiento = request.POST['fecha_nacimiento'] 
        clave = request.POST['password']
    if not checkUser(usuario):
        nuevo_usuario = Usuario(usuario=usuario, nombre=nombres, apellido=apellidos, genero=genero, correo =correo , clave=clave ,fecha_nacimiento=fecha_nacimiento)
        nuevo_usuario.save()
        return render(request, 'register.html',{'msg':"usuario agregado"})
    else:
        return render(request, 'register.html',{'msg':"Usuario existente"})

def checkUser(usuario):
    try:
        return Usuario.objects.get(usuario=usuario)
    except Exception:
        return False


def main_view(request):
    usuario= checkUser(request.POST['usuario'])
    
    if not usuario:
        return render(request, 'login.html',context={'msg':"Usuario no existente"})
    if usuario.clave != request.POST['password']:
        return render(request, 'login.html',context={'msg':"Clave incorrecta"})   
    rutinas= Rutina.objects.filter(Q(genero='A') | Q(genero=usuario.genero)  ).order_by('numeroLikes')     
    return render(request, 'main_view.html',{'usuario':usuario,'rutinas':rutinas, 'clasificacion':getClasificationsOfRutines()})
    
    
def getClasificationsOfRutines():
    rutinas = Rutina.objects.all()
    clasificaciones = set()
    for rutina in rutinas:
        clasificaciones.add(rutina.clasificacion)
    return clasificaciones

def filtrarRutina(request):
    print(request.POST)
    usuario= checkUser(request.POST['usr'])
    
    if request.POST['clasificacion']=="todas":
        rutinas= Rutina.objects.filter( Q(sitio=request.POST['sitio']) & (Q(genero='A') | Q(genero=usuario.genero))  ).order_by('numeroLikes')     
        return render(request, 'main_view.html',{'usuario':usuario,'rutinas':rutinas, 'clasificacion':getClasificationsOfRutines()})

    rutinas = Rutina.objects.filter(Q(sitio=request.POST['sitio']) & Q(clasificacion=request.POST['clasificacion']) & (Q(genero='A') | Q(genero=usuario.genero)) ).order_by('numeroLikes')  
    return render(request, 'main_view.html',{'usuario':usuario,'rutinas':rutinas, 'clasificacion':getClasificationsOfRutines()})

def exercisesList(request):
    usuario= checkUser(request.POST['user'])
    ejercicios= EjercicioXRutina.objects.filter(Q(rutina=request.POST['rutineId']))
    rutina =Rutina.objects.get(id=request.POST['rutineId'])
 
    return render(request, 'exercisesList.html',{'usuario':usuario,'ejercicios':ejercicios, 'rutina':rutina})

