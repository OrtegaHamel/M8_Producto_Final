from django.contrib import admin
from django.contrib.auth.views import LoginView
from eventos.views import home_publico
from django.urls import path, include
from django.conf.urls import handler403

def custom_permission_denied(request, exception):
    from django.shortcuts import render
    return render(request, '403.html', status=403)

handler403 = custom_permission_denied


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('bandas/', include('bandas.urls')),
    path('eventos/', include('eventos.urls')),
    path('', home_publico, name='home_publico'),  # Home público como raíz
]
