from django.contrib import admin
from .models import Usuario, Rutina

# Register your models here.

@admin.register(Usuario)
class WitAdmin(admin.ModelAdmin):
    
    list_display = ("id", "usuario" ,"nombre", "apellido", "correo", "genero", "clave", "fecha_nacimiento")

@admin.register(Rutina)
class WitAdmin(admin.ModelAdmin): 
    list_display = ("id", "usuario" , "genero" ,"clasificacion", "descripcion", "numeroLikes")