from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import *
from datetime import datetime

class Estudiante(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    datos = [cedula, nombre, usuario, contraseña]

    def findEst(self, user, passw):
        try:
            p = Estudiante.objects.get(usuario=user, contraseña=passw)
            return p
        except ObjectDoesNotExist:
            return None


class Implemento(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    cantidad_disponible = models.IntegerField()
    cantidad_prestada = models.IntegerField()
    datos = [nombre, cantidad_disponible, cantidad_prestada]

    def buscarExistencias(self, nombre):
        try:
            p = Implemento.objects.get(nombre=nombre)
            return p
        except ObjectDoesNotExist:
            return None

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    implemento = models.CharField(max_length=50)
    estudiante = models.IntegerField()
    hora_despacho = models.DateTimeField()
    hora_devuelta = models.DateTimeField(default=None, null=True)
    datos = [id, implemento, estudiante,hora_despacho,hora_devuelta]

    def CreatePending(self, estudiante, implemento):
        fecha_inicial = datetime.now()
        objeto = Prestamo(estudiante=estudiante, implemento=implemento, hora_despacho=fecha_inicial)
        objeto.save()

    def findPending(self, estudiante):
        try:
            p = Prestamo.objects.get(estudiante=estudiante, hora_devuelta=None)
            if p.hora_devuelta == None:
                return p
        except ObjectDoesNotExist:
            return False

    def anulatePending(self, estudiante):
        p = Prestamo.objects.get(estudiante=estudiante, hora_devuelta=None)
        p.hora_devuelta = datetime.now()
        p.save()
