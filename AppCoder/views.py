from django import http
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto= f"Curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return HttpResponse("esta es la pagina de profesores")

def estudiantes(request):
    return HttpResponse("esta es la pagina de estudiantes")

def cursos(request):
    return HttpResponse("esta es la pagina de cursos")

def entregables(request):
    return HttpResponse("esta es la pagina de entregables")