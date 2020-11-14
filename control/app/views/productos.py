#Serializador
from ..serializers.productos import ProductoSerializer
#Modelo
from ..models.productos import Producto
#Genéricas
from rest_framework.generics import ListAPIView, get_object_or_404, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from ..permissions.control import IsOwner, IsNotOwner

class CrearProducto (CreateAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductoSerializer
    model = Producto
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        context = super(CrearProducto, self).get_serializer_context()
        return context

class ListarProducto (ListAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductoSerializer
    model = Producto
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_context(self):
        context = super(ListarProducto, self).get_serializer_context()
        return context

class ActualizarProducto (UpdateAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductoSerializer
    model = Producto
    permission_classes = [IsAdminUser|IsOwner]
    
    def get_serializer_context(self):
        context = super(ActualizarProducto, self).get_serializer_context()
        return context

class EliminarProducto (DestroyAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductoSerializer
    model = Producto
    permission_classes = [IsAdminUser|IsOwner]
    
    def get_serializer_context(self):
        context = super(EliminarProducto, self).get_serializer_context()
        return context

class VerProducto (RetrieveAPIView):
    serializer_class = ProductoSerializer
    model = Producto
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        query = Producto.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
    
    def get_serializer_context(self):
        context = super(VerProducto, self).get_serializer_context()
        return context