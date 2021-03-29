from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .models import Usuario


@csrf_exempt
def loginView(request):
    return render(request, 'login.html', context={'msg': 'soy el login'})


def index(request):
    return render(request, 'index.html', context={'msg': 'HOME'})


def mainView(request):
    return render(request, 'main_view.html', context={})


def registerView(request):
    return render(request, 'register.html', context={'msg': 'SIGN IN'})


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
        Usuario.objects.get(usuario=usuario)
        return True
    except Exception:
        return False
    

