from django.urls import path
from . import views

app_name = 'bandas'
urlpatterns = [
    path('', views.lista_bandas, name='lista_bandas'),
    path('crear/', views.crear_banda, name='crear_banda'),
    path('editar/<int:banda_id>/', views.editar_banda, name='editar_banda'),
    path('eliminar/<int:banda_id>/', views.eliminar_banda, name='eliminar_banda'),
]
