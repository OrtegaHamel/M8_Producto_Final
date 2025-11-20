from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('bandas/', include('bandas.urls')),
    path('eventos/', include('eventos.urls')),
    path('', LoginView.as_view(template_name='usuarios/login.html'), name='home'),
]
