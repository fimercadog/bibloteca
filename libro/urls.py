from django.urls import path
from libro.views import *

urlpatterns = [
    path('crear_autor/', crearAutorView, name='crear_autor'),
    path('listar_autor/', listarAutorView, name='lista_autor'),
    path('editar_autor/<int:id>', editarAutorView, name='editar_autor')
]
