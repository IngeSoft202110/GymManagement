from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .models import Usuario,Rutina, Ejercicio, EjercicioXRutina
from django.db.models import Q

@csrf_exempt
def loginView(request):
    return render(request, 'login.html')


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

def crearRutinaView(request):
    usuario= checkUser(request.POST['usr'])
    if not usuario:
        return render(request, 'login.html',context={'msg':"Usuario no existente"})
    return render(request,'crearRutina.html',{'usuario':usuario, 'clasificacion':getClasificationsOfRutines()})

def agregarEjercicioXRutinaView(request):
    usuario= checkUser(request.POST['usr'])
    if request.method == 'POST':
        genero = request.POST['genero']
        clasificacion = request.POST['clasificacion']
        descripcion = request.POST['descripcion']
        numeroLikes = 0
        dificultad = request.POST['dificultad']
        lugar = request.POST['sitio']
        nueva_rutina = Rutina(usuario= usuario, genero=genero, clasificacion=clasificacion,descripcion=descripcion,numeroLikes=numeroLikes,dificultad=dificultad,sitio=lugar)
        nueva_rutina.save()
    return render(request,'agregarEjercicioXRutina.html',{'ejerciciosRutina':"",'usuario':usuario,'rutina':nueva_rutina, 'ejercicios':getTodosEjercicios()})

def agregarEjercicioXRutinaView2(request):
    usuario= checkUser(request.POST['usr'])
    ejercicio = request.POST['ejercicio']
    tipoEjercicio = getEjercicio(ejercicio)
    rutina2 = Rutina.objects.get(id=request.POST['rutina'])
    nuevo_ejercicioxrutina = EjercicioXRutina(rutina=rutina2,ejercicio=tipoEjercicio)
    nuevo_ejercicioxrutina.save()
    return render(request,'agregarEjercicioXRutina.html',{'ejerciciosRutina':getEjercicioXRutina(rutina2),'usuario':usuario,'rutina':rutina2,'ejercicios':getTodosEjercicios()})

def getRutina(idRutina):
    rutinas = Rutina.objects.all()
    for rutina in rutinas:
        if rutina.id == idRutina:
            return rutina
    return 0
def getEjercicio(nombreEjercicio):
    ejercicios = Ejercicio.objects.all()
    for ejercicio in ejercicios:
        if ejercicio.nombre == nombreEjercicio:
            return ejercicio
    return 0


def getEjercicioXRutina(rutina):
    ejerciciosxrutinas = EjercicioXRutina.objects.all()
    ejerciciosxrutinasTodos = set()
    for ejerciciosxrutina in ejerciciosxrutinas:
        if ejerciciosxrutina.rutina == rutina:
            ejerciciosxrutinasTodos.add(ejerciciosxrutina.ejercicio.nombre)
    return ejerciciosxrutinasTodos
    

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
    
def getTodosEjercicios():
    ejercicios = Ejercicio.objects.all()
    ejerciciosTodos = set()
    for ejercicio in ejercicios:
        ejerciciosTodos.add(ejercicio.nombre)
    return ejerciciosTodos

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

