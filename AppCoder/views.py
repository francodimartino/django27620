from django import http
from django.shortcuts import render

from .models import Curso, Estudiante, Profesor, Entregable, Avatar
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfeFormulario, UserRegistrationForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto= f"Curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

    


def inicio(request):

    avatar=Avatar.objects.filter(user=request.user)
    return render(request, 'AppCoder/inicio.html' ,{'url': avatar[0].avatar.url})

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')



def entregables(request):
    return render(request, 'AppCoder/entregables.html')


#-----------------------------------------------------------------------------
def cursos(request):

    if request.method == 'POST':

        miFormulario=CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso=Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=CursoFormulario()
    return render(request, 'AppCoder/cursos.html', {'formulario':miFormulario})
#-------------------------------------------------------------------

def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')


def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision=comision)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos, 'comision':comision})
    else:
        respuesta="No se ingreso ninguna comision"
        return render(request, 'AppCoder/resultadosBusqueda.html', {'respuesta':respuesta})





        
        

    return render(request, 'AppCoder/cursosFormulario.html')




def leerProfesores(request):
    profesores=Profesor.objects.all()
    contexto={'profesores':profesores}
    
    return render(request, 'AppCoder/profesores.html', contexto)

@login_required
def eliminarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    profesor.delete()

    profesores=Profesor.objects.all()
    contexto={'profesores':profesores}
        
    return render(request, 'AppCoder/profesores.html', contexto)

#-------------------------------------------------------------------
def editarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    if request.method == 'POST':
        formulario=ProfeFormulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            profesor.nombre=informacion['nombre']
            profesor.apellido=informacion['apellido']
            profesor.email=informacion['email']
            profesor.profesion=informacion['profesion']
            profesor.save()
            #luego muestro la lista de profes de nuevo
            profesores=Profesor.objects.all()
            contexto={'profesores':profesores}
        
            return render(request, 'AppCoder/profesores.html', contexto)
    else:
        formulario=ProfeFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
    return render(request, 'AppCoder/editarProfesor.html', {'formulario':formulario, 'nombre':nombre})



#-------------------------------------------------------------------

class EstudiantesList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes.html'

class EstudianteDetalle(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')#
    fields=['nombre', 'apellido', 'email']

class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')#
    fields=['nombre', 'apellido', 'email']

class EstudianteEliminacion(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')#
    fields=['nombre', 'apellido', 'email']



    
#------------LOGIN------
def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
            user=authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/inicio.html', {'usuario':usuario, 'mensaje':'Bienvenido al sistema'})
            else:
                return render(request, 'AppCoder/login.html', {'formulario':formulario, 'mensaje':'USUARIO INCORRECTO, VUELVA A LOGUEAR'})
        else:
            return render(request, 'AppCoder/login.html', {'formulario':formulario, 'mensaje':'FORMULARIO INVALIDO, VUELVA A LOGUEAR'})
    
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'formulario':formulario})


def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':f'USUARIO: {username} CREADO EXITOSAMENTE'})
        else:
            return render(request, 'AppCoder/inicio.html', {'mensaje':'NO SE PUDO CREAR EL USUARIO'})
    else:
        formulario = UserRegistrationForm()
        return render(request, 'AppCoder/register.html', {'formulario':formulario})

#-------------------------------------------------------------------


@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'AppCoder/inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppCoder/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})

#-------------------------------------------------------------------


@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():

            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.avatar):
                avatarViejo.delete()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AppCoder/inicio.html', {'usuario':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppCoder/agregarAvatar.html', {'formulario':formulario, 'usuario':user})
