from rest_framework import serializers
from libreria.models import Libro, Autor, Lenguaje, Genero, Ejemplar

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id' , 'titulo', 'summary', 'isbn', 'genero', 'lenguaje', 'autor']
        depth = 1
    
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id' ,'genero']

class LenguajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lenguaje
        fields = ['id' ,'idioma']
    
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id' ,'nombre', 'apellido', 'fecha_nacimiento']

class EjemplarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejemplar
        fields = ['id' , 'libro', 'observacion', 'fecha', 'estado']
