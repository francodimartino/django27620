from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    
   # path('creaCurso', curso),
    
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
   # path('cursosFormulario/', cursosFormulario, name='cursosFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
    

]