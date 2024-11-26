from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Biografía opcional
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Imagen de perfil

    def _str_(self):
        return self.username
    