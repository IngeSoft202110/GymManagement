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
    CLASIFICATIONS=(
        ('PIERNA','PIERNA'),
        ('BRAZO','BRAZO'),
        ('HOMBRO','HOMBRO'),
        ('ESPALDA','ESPALDA'),
        ('ABDOMEN','ABDOMEN'),
        ('CARDIO','CARDIO')
    )
    DIFFICULTY=(
        ('PRINCIPIANTE','PRINCIPIANTE'),
        ('INTERMEDIO','INTERMEDIO'),
        ('AVANZADO','AVANZADO'),   
    )
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE, default=1)
    genero=models.CharField(max_length=1, null=False, choices=GENDERS )
    clasificacion= models.CharField(max_length=20, null=False, choices=CLASIFICATIONS, default="PIERNA")
    descripcion=models.CharField(max_length=500, null=False )
    numeroLikes=models.IntegerField( null=False )
    dificultad= models.CharField(max_length=20, null=False, choices=DIFFICULTY, default="PRINCIPIANTE")
    def __str__(self):
        return f"{self.id}, {self.usuario}, {self.genero}, {self.clasificacion}, {self.descripcion}, {self.numeroLikes}, {self.dificultad} "

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
