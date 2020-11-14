#Permisos para la venta de productos

from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsOwner(BasePermission):
    """
    Verifica si el usuario que solicita es el creador del producto.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.vendedor == request.user

class IsNotOwner(BasePermission):
    """
    Sólo usuarios que no crearon el producto pueden comprarlo
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return not obj.vendedor == request.user