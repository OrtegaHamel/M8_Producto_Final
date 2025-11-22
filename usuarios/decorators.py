from django.core.exceptions import PermissionDenied

def grupo_required(*group_names):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            # Permitir acceso si el usuario es superusuario
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            # Verificar si el usuario pertenece a alguno de los grupos requeridos
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrap
    return decorator
