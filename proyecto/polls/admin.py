from django.contrib import admin
from .models import Usuario, Rutina, Comentario, Ejercicio, EjercicioXRutina

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario" ,"nombre", "apellido", "correo", "genero", "clave", "fecha_nacimiento")

@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario" , "genero" ,"clasificacion", "descripcion", "numeroLikes", "dificultad", "sitio", "series")

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin): 
    list_display = ("id", "nombre" , "descripcion" ,"linkYoutube", "peso", "repeticiones")

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario" , "rutina" ,"comentario")

@admin.register(EjercicioXRutina)
class EjercicioXRutinaAdmin(admin.ModelAdmin): 
    list_display = ("id", "ejercicio" ,"rutina")