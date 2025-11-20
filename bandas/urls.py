from django.urls import path
from . import views

app_name = 'bandas'
urlpatterns = [
    path('', views.lista_bandas, name='lista_bandas'),
    path('crear/', views.crear_banda, name='crear_banda'),
]
