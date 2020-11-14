from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario (AbstractUser):
    VENDEDOR = 1
    USUARIO = 2
    
    ROLES = (
        (VENDEDOR, 'Vendedor'),
        (USUARIO, 'Usuario')
    )
    
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con este nombre de usuario.'
        }
    )
    
    USERNAME_FIELD = 'username'
    
    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique' : 'Ya existe un usuario con este correo.'
        }
    )
    
    rol = models.IntegerField(choices=ROLES, default=USUARIO)
    
    is_verified = models.BooleanField(
        'usuario', 
        default=True, 
        help_text='Verdadero si el usuario verificó su registro.'
    )
    
    is_active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username