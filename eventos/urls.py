from django.urls import path
from . import views

app_name = 'eventos'
urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
]
