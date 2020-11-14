#Serializador
from ..serializers.usuarios import UserSerializer
#Modelo
from ..models.usuarios import Usuario
#Respuesta de Servidor
from rest_framework.response import Response
#Autenticación
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
#Vistas empleadas
from rest_framework import viewsets
#Genéricas
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, get_object_or_404, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CrearUsuario (CreateAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = []

class ListarUsuarios (ListAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = [IsAuthenticated]

class ActualizarUsuario (UpdateAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = [IsAdminUser]

class EliminarUsuario (DestroyAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = [IsAdminUser]

class VerUsuario (RetrieveAPIView):
    serializer_class = UserSerializer
    model = Usuario
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = Usuario.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

class LoginView (APIView):
    permission_classes = []
    
    def post (self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user:
            return Response(
                {'token': user.auth_token.key}
            )
        else:
            return Response(
                {'error': 'Credenciales inválidas. Inicie sesión.'},
                status= status.HTTP_400_BAD_REQUEST
            )