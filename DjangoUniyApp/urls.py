from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('estudiante/<str:pk>/',views.estudiante_views, name='estudiante'),


 path('ejemplo/',views.ejemplo_views, name='ejemplo'),

 path('Productos/',views.productos_views, name='productos'),

 path('logo/',views.logo_views, name='logo'),
 
]