#Serializador
from rest_framework import serializers
#Modelo
from ..models.usuarios import Usuario
#Token autenticación REST framework
from rest_framework.authtoken.models import Token

class UserSerializer (serializers.ModelSerializer):
    """
    Serializador para datos de usuarios del sistema.
    """
    
    class Meta:
        model = Usuario
        fields = [
            'id', 'first_name',
            'last_name', 'username',
            'email', 'rol',
            'password', 'is_staff',
            'is_verified', 'is_active'
        ]
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def create(self, validated_data):
        user = Usuario(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            rol = validated_data['rol'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user