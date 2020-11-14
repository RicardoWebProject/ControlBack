from django.urls import path
#vistas Productos
from .views.productos import CrearProducto, ListarProducto, EliminarProducto, ActualizarProducto, VerProducto
#Vistas Usuarios
from .views.usuarios import CrearUsuario, ListarUsuarios, ActualizarUsuario, EliminarUsuario, VerUsuario, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    #URL de Usuarios
    path('usuarios/crear/', CrearUsuario.as_view(), name='crearUsuario'),
    path('usuarios/listar/', ListarUsuarios.as_view(), name='listarUsuarios'),
    path('usuarios/actualizar/<pk>', ActualizarUsuario.as_view(), name='actualizarUsuario'),
    path('usuarios/eliminar/<pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('usuarios/ver/<pk>', VerUsuario.as_view(), name='verUsuario'),
    #URL de Productos
    path('producto/crear', CrearProducto.as_view(), name = 'crearproducto'),
    path('producto/mostrar/', ListarProducto.as_view(), name = 'listarproducto'),
    path('producto/ver/<pk>', VerProducto.as_view(), name = 'verproducto'),
    path('producto/eliminar/<pk>', EliminarProducto.as_view(), name = 'eliminarproducto'),
    path('producto/actualizar/<pk>', ActualizarProducto.as_view(), name = 'actualizarproducto'),
]