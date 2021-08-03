from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 context = {'clase': 'Aprendiendo Django'}
 return render(request, 'listado_estudiantes.html', context)

def estudiante(request, pk):
 return HttpResponse("Soy el estudiante numero: " + str(pk))


def ejemplo_views(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
 return render(request,'ejemplo.html',locals())