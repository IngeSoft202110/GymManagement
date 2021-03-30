from django.db import models
from datetime import date
# Create your models here.

class Usuario(models.Model):
    GENDERS = (
        ('M','masculino'),
        ('F','femenino'),
    )
    usuario = models.CharField(max_length=20, null=False)
    nombre = models.CharField(max_length=264, null= False)
    apellido = models.CharField(max_length=264, null=False)
    correo = models.EmailField(null=False)
    genero = models.CharField(max_length=1, null=False, choices=GENDERS)
    clave = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField()


    def __str__(self):
        return f"{self.id}, {self.usuario}, {self.nombre}, {self.apellido}, {self.correo}, {self.genero}, {self.clave}, {self.fecha_nacimiento} "
        
class Rutina(models.Model):
    GENDERS = (
        ('M','masculino'),
        ('F','femenino'),
        ('A','ambos'),
    )
    genero=models.CharField(max_length=1, null=False, choices=GENDERS )
    clasificacion= models.CharField(max_length=30, null=False )
    descripcion=models.CharField(max_length=100, null=False )
    numeroLikes=models.IntegerField( null=False )
    def __str__(self):
        return f"{self.id}, {self.genero}, {self.clasificacion}, {self.descripcion}, {self.numeroLikes} "

#class Ejercicio(models.Model):
#   nombreEjercicio= models.CharField(max_length=30, null=False )
#   descripcionEjercicio= models.CharField(max_length=100, null=False )
#   linkYoutube= models.CharField(max_length=100, null=False )
#   def __str__(self):
#        return f"{self.id}, {self.nombreEjercicio}, {self.descripcionEjercicio}, {self.linkYoutube} "

#class Comentario(models.Model):
#    comentario = models.CharField(max_length=100, null=False )
#    def __str__(self):
#        return f"{self.id}, {self.comentario} "

#class RutinaRealizada(models.Model):
#    fecha = models.DateField()     
#    def __str__(self):
#        return f"{self.id}, {self.fecha} "
