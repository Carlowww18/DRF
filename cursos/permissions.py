from rest_framework import permissions

class EhSuperUsuario(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            else:
                return False
        return True