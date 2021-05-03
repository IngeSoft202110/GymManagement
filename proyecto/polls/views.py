from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .models import Usuario, Rutina, Ejercicio, EjercicioXRutina
from .models import Comentario, Sala, Mensaje, UsuarioxRutina, Like

from django.db.models import Q

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
    return render(request, 'exercise.html', {'ejercicios': ejercicios})

def exercisesListView(request):
    return render(request, 'exercisesList.html')

def exercisesListRutinaView(request):
    return render(request, 'exercisesListRutina.html')

def crearRutinaView( request ):
    usuario = checkUser(request.POST['usr'])
    if not usuario:
        return render(request, 'login.html', context={'msg': "Usuario no existente"})
    return render(request, 'crearRutina.html', {'usuario': usuario, 'clasificacion': getClasificationsOfRutines()})



def agregarEjercicioXRutinaView(request):
    usuario = checkUser(request.POST['usr'])
    if request.method == 'POST':
        genero = request.POST['genero']
        clasificacion = request.POST['clasificacion']
        descripcion = request.POST['descripcion']
        numeroLikes = 0
        dificultad = request.POST['dificultad']
        lugar = request.POST['sitio']
        nueva_rutina = Rutina(usuario=usuario, genero=genero, clasificacion=clasificacion,
                              descripcion=descripcion, numeroLikes=numeroLikes, dificultad=dificultad, sitio=lugar)
        nueva_rutina.save()
    return render(request, 'agregarEjercicioXRutina.html', {'ejerciciosRutina': "", 'usuario': usuario, 'rutina': nueva_rutina, 'ejercicios': getTodosEjercicios()})

def agregarEjercicioXRutinaView2(request):
    usuario = checkUser(request.POST['usr'])
    ejercicio = request.POST['ejercicio']
    tipoEjercicio = getEjercicio(ejercicio)
    rutina2 = Rutina.objects.get(id=request.POST['rutina'])
    nuevo_ejercicioxrutina = EjercicioXRutina(
        rutina=rutina2, ejercicio=tipoEjercicio)
    nuevo_ejercicioxrutina.save()
    return render(request, 'agregarEjercicioXRutina.html', {'ejerciciosRutina': getEjercicioXRutina(rutina2), 'usuario': usuario, 'rutina': rutina2, 'ejercicios': getTodosEjercicios()})

def getTodosEjercicios():
    ejercicios = Ejercicio.objects.all()
    ejerciciosTodos = set()
    for ejercicio in ejercicios:
        ejerciciosTodos.add(ejercicio.nombre)
    return ejerciciosTodos

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
        nuevo_usuario = Usuario(usuario=usuario, nombre=nombres, apellido=apellidos,
                                genero=genero, correo=correo, clave=clave, fecha_nacimiento=fecha_nacimiento)
        nuevo_usuario.save()
        return render(request, 'register.html', {'msg': "usuario agregado"})
    else:
        return render(request, 'register.html', {'msg': "Usuario existente"})

def checkUser(usuario):
    try:
        return Usuario.objects.get(usuario=usuario)
    except Exception:
        return False

def main_view(request):

    if not checkPostRequest(request):
        return render(request, 'login.html')
    usuario = checkUser(request.POST['usuario'])
    if not usuario:
        return render(request, 'login.html', context={'msg': "Usuario no existente"})

    rutinas = Rutina.objects.filter(Q(genero='A') | Q(
        genero=usuario.genero)).order_by('numeroLikes').reverse()
    print(request.POST)
    if not "password" in request.POST:
        return render(request, 'main_view.html', {'usuario': usuario, 'rutinas': rutinas, 'clasificacion': getClasificationsOfRutines()})

    if usuario.clave != request.POST['password']:
        return render(request, 'login.html', context={'msg': "Clave incorrecta"})

    return render(request, 'main_view.html', {'usuario': usuario, 'rutinas': rutinas, 'clasificacion': getClasificationsOfRutines()})

def getClasificationsOfRutines():
    rutinas = Rutina.objects.all()
    clasificaciones = set()
    for rutina in rutinas:
        clasificaciones.add(rutina.clasificacion)
    return clasificaciones

def filtrarRutina(request):
    if not checkPostRequest(request):
        return render(request, 'login.html')
    usuario = checkUser(request.POST['usr'])

    if request.POST['clasificacion'] == "todas":
        rutinas = Rutina.objects.filter(Q(sitio=request.POST['sitio']) & (
            Q(genero='A') | Q(genero=usuario.genero))).order_by('numeroLikes')
        return render(request, 'main_view.html', {'usuario': usuario, 'rutinas': rutinas, 'clasificacion': getClasificationsOfRutines()})

    rutinas = Rutina.objects.filter(Q(sitio=request.POST['sitio']) & Q(clasificacion=request.POST['clasificacion']) & (
        Q(genero='A') | Q(genero=usuario.genero))).order_by('numeroLikes')
    return render(request, 'main_view.html', {'usuario': usuario, 'rutinas': rutinas, 'clasificacion': getClasificationsOfRutines()})

def exercisesList(request):
    if not checkPostRequest(request):
        return render(request, 'login.html')
    usuario = checkUser(request.POST['user'])
    ejercicios = EjercicioXRutina.objects.filter(
        Q(rutina=request.POST['rutineId']))
    rutina = Rutina.objects.get(id=request.POST['rutineId'])

    return render(request, 'exercisesList.html', {'usuario': usuario, 'ejercicios': ejercicios, 'rutina': rutina})


def exercisesListRutina(request):
    if not checkPostRequest(request):
        return render(request, 'login.html')
    usuario = checkUser(request.POST['user'])
    ejercicios = EjercicioXRutina.objects.filter(
        Q(rutina=request.POST['rutineId']))
    rutina = Rutina.objects.get(id=request.POST['rutineId'])

    return render(request, 'exercisesListRutina.html', {'usuario': usuario, 'ejercicios': ejercicios, 'rutina': rutina})


def comentar(request):
    if not checkPostRequest(request):
        return render(request, 'login.html')
    usuario = checkUser(request.POST['usuario'])
    rutina = Rutina.objects.get(id=int(request.POST["rutina"]))
    if request.POST['comentario']:
        nuevo_comentario = Comentario(
            usuario=usuario, rutina=rutina, comentario=request.POST["comentario"])
        nuevo_comentario.save()
        return JsonResponse({"msg": "comentario agregado"}, status=200)
    else:
        return JsonResponse({"msg": "no hubo comentario"}, status=200)

def verComentarios(request):
    if not checkPostRequest(request):
        return render(request, 'login.html')
    usuario = checkUser(request.POST['usuario'])
    rutina = Rutina.objects.get(id=int(request.POST["rutina"]))
    comentarios = Comentario.objects.filter(Q(rutina=rutina))
    return render(request, "coments.html", {'usuario': usuario, 'comentarios': comentarios, 'rutina': rutina})

def verChats(request):
    if not checkPostRequest(request):
        return render(request, 'login.html')
    salas = Sala.objects.filter(Q(usuario1=request.POST['usuario']) | Q(
        usuario2=request.POST['usuario'])).distinct()

    return render(request, "bandejaMensajes.html", {'usuario': checkUser(request.POST['usuario']), 'salas': salas})

def checkPostRequest(request):
    if not request.POST:
        return False
    return True

def guardarRutinaView(request):
    usuario= checkUser(request.POST['usuario'])
    usuarioxrutina = UsuarioxRutina.objects.all()
    listado = set()
    for rutina in usuarioxrutina:
        if rutina.usuario == usuario:
            listado.add(rutina.rutina)
    return render(request, 'guardarRutina.html', {'rutinas':listado, 'usuario':usuario})

def irSala(request):
    print(request.POST)
    usuario = checkUser(request.POST['usuario'])
    messages = Mensaje.objects.filter(sala=request.POST['sala'])

    return render(request, 'sala.html', {'sala': request.POST['sala'], 'usuario': usuario, 'messages': messages})

def seguirRutina(request):
    print(request.POST)
    usuario = checkUser(request.POST['usuario'])
    rutina = Rutina.objects.get(id=request.POST["rutina"])
    print(usuario)
    print(rutina)
    buscarUsuarioXRutina = UsuarioxRutina.objects.filter(
        Q(usuario=usuario) & Q(rutina=rutina))
    print(buscarUsuarioXRutina)
    if not buscarUsuarioXRutina:
        usuarioxRutina = UsuarioxRutina(rutina=rutina, usuario=usuario)
        usuarioxRutina.save()

    return JsonResponse({"msg": "rutina agregada"}, status=200)

def like(request):
    print(request.POST)
    usuario = checkUser(request.POST['usuario'])
    rutina = Rutina.objects.get(id=request.POST["rutina"])
    print(usuario)
    print(rutina)
    buscarLike = Like.objects.filter(
        Q(usuario=usuario) | Q(rutina=rutina))
    print(buscarLike)
    if not buscarLike:
        rutina.numeroLikes+=1
        rutina.save()
        like = Like(rutina=rutina, usuario=usuario)
        like.save()
        

    return JsonResponse({"msg": "like agregado"}, status=200)
