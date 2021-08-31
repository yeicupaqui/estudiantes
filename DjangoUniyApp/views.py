from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    context = {'clase': 'Aprendiendo Django'}
    return render(request, 'listado_estudiantes.html', context)

def estudiante_views(request, pk):
    return HttpResponse("Soy el estudiante numero: " + str(pk))


def ejemplo_views(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    return render(request,'ejemplo.html',locals())

def productos_views(request): 
    lista = estudiante.objects.all()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    return render(request,'productos.html',locals())

def logo_views(request):
    return render(request,'logo.html',locals())


