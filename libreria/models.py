from django.db import models

# Create your models here.
from django.db import models
import uuid 

class Genero(models.Model):
    genero = models.CharField(max_length=200, help_text="")

    def __str__(self):
        return self.genero
    
class Lenguaje(models.Model):
    idioma = models.CharField(max_length=200, help_text="")

    def __str__(self):
        return self.idioma
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)


    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellido)
    
class Libro(models.Model):

    titulo = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="")

    isbn = models.CharField('ISBN',max_length=13, help_text='')

    #########################
    ######  Relaciones
    #########################
    genero = models.ManyToManyField(Genero, help_text="")
    lenguaje = models.ManyToManyField(Lenguaje, help_text="")
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titulo


class Ejemplar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="")
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True)
    observacion = models.CharField(max_length=200)
    fecha = models.DateField(null=True, blank=True)

    estados_libro = (
        ('m', 'Mantenimiento'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )

    estado = models.CharField(max_length=1, choices=estados_libro, blank=True, default='m', help_text='')

    def __str__(self):
        return '%s (%s)' % (self.id,self.libro.titulo)