from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from libreria.models import Libro, Autor, Lenguaje, Genero, Ejemplar
from .serializers import LibroSerializer, AutorSerializer, LenguajeSerializer, GeneroSerializer, EjemplarSerializer

class GeneroView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        genero = Genero.objects.all()
        serializer = GeneroSerializer(genero, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = GeneroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LenguajeView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Lenguaje.objects.all()
    serializer_class = LenguajeSerializer
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        lenguaje = Lenguaje.objects.all()
        serializer = LenguajeSerializer(lenguaje, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = LenguajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AutorView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        autor = Autor.objects.all()
        serializer = AutorSerializer(autor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LibroView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer   
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        libro = Libro.objects.all()
        serializer = LibroSerializer(libro, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EjemplarView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Ejemplar.objects.all()
    serializer_class = EjemplarSerializer
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        ejemplar = Ejemplar.objects.all()
        serializer = EjemplarSerializer(ejemplar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EjemplarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
