from django.contrib import admin
from .models import Usuario, Rutina, Comentario, Ejercicio, UsuarioxRutina
from .models import  EjercicioXRutina, Sala, Mensaje, Like, Historial

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ( "id" , "usuario" ,"nombre", "apellido", "correo", "genero", "clave", "fecha_nacimiento")

@admin.register(Rutina )
class RutinaAdmin( admin.ModelAdmin): 
    list_display = ( "id", "usuario" , "genero" ,"clasificacion", "descripcion", "numeroLikes", "dificultad", "sitio")

@admin.register( Ejercicio)
class EjercicioAdmin(admin.ModelAdmin): 
    list_display = ("id" , "nombre" , "descripcion" ,"linkYoutube", "peso", "repeticiones", "series")

@admin.register(Comentario)
class ComentarioAdmin( admin.ModelAdmin): 
    list_display = ("id","comentario" , "fecha" ,"usuario" , "rutina" )

@admin.register(EjercicioXRutina)
class EjercicioXRutinaAdmin(admin.ModelAdmin): 
    list_display = ("id", "ejercicio" ,"rutina")

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario1" ,"usuario2")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario" ,"rutina")

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin): 
   list_display = ("id", "fecha" , "mensaje", "sala")

@admin.register(UsuarioxRutina)
class UsuarioxRutinaAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario" ,"rutina")

@admin.register(Historial)
class UsuarioxRutinaAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario" ,"ejercicio", "fecha")

