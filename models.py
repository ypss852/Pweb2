from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def _str_(self):
        return self.username
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def _str_(self):
        return f"{self.titulo} de {self.autor}"