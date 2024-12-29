from django.db import models

# Create your models here.
class Mensaje(models.Model):
    nombres = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    mensaje = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)
