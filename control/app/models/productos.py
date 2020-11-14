#Usuario
from django.conf import settings
#Modelos
from django.db import models

class Producto (models.Model):
    ACTIVO = 1
    INACTIVO = 0
    
    ESTADO = (
        (ACTIVO, 'Producto disponible'),
        (INACTIVO, 'Producto no disponible')
    )
    
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.FloatField()
    estado = models.IntegerField(choices=ESTADO, default=ACTIVO)
    createdAt = models.DateField(auto_now=True)
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='owner',
        on_delete=models.CASCADE,
        blank=True, null=True
    )