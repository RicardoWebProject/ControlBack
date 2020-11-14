#Serializador
from rest_framework import serializers
#Modelo
from ..models.productos import Producto

class ProductoSerializer (serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default = serializers.CurrentUserDefault(), read_only=True)
    
    class Meta:
        model = Producto
        fields = [
            'nombre', 'descripcion',
            'precio', 'estado',
            'createdAt', 'owner'
        ]
        read_only_fields = ['createdAt']