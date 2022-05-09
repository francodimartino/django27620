from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    
   # path('creaCurso', curso),
    
    path('cursos/', cursos, name='cursos'),
    path('profesores/', leerProfesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
   # path('cursosFormulario/', cursosFormulario, name='cursosFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name='eliminarProfesor'),
    path('editarProfesor/<nombre>', editarProfesor, name='editarProfesor'),

    path('estudiante/list/', EstudiantesList.as_view(), name='estudiante_listar'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/editar/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='estudiante_borrar'),
    

]