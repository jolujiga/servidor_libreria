from django.conf.urls import url

from . import views

from django.urls import path
from libreria import views

urlpatterns = [
    path('Genero/', views.GeneroView.as_view(), name='Genero'),
    path('Lenguaje/', views.LenguajeView.as_view(), name='Lenguaje'),
    path('Autor/', views.AutorView.as_view(), name='Autor'),
    path('Libro/', views.LibroView.as_view(), name='Libro'),
    path('Ejemplar/', views.EjemplarView.as_view(), name='Ejemplar'),
]