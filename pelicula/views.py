from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from pelicula.models import Pelicula
from pelicula.serializers import PeliculaSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def pelicula_list(request):
    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        
        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            peliculas = peliculas.filter(nombre__icontains=pelicula)
        
        pelicula_serializer = PeliculaSerializer(peliculas, many=True)
        return JsonResponse(pelicula_serializer.data, safe=False)
    elif request.method == 'POST':
        pelicula_data = JSONParser().parse(request)
        pelicula_serializer = PeliculaSerializer(data=pelicula_data)
        if pelicula_serializer.is_valid():
            pelicula_serializer.save()
            return JsonResponse(pelicula_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pelicula_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def pelicula_detail(request, pk):
    # find tutorial by pk (id)
    pelicula = Pelicula.objects.get(pk=pk)
    if request.method == 'GET': 
        pelicula_serializer = PeliculaSerializer(pelicula) 
        return JsonResponse(pelicula_serializer.data) 
    elif request.method == 'PUT': 
        pelicula_data = JSONParser().parse(request) 
        pelicula_serializer = PeliculaSerializer(pelicula, data=pelicula_data) 
        if pelicula_serializer.is_valid(): 
            pelicula_serializer.save() 
            return JsonResponse(pelicula_serializer.data) 
        return JsonResponse(pelicula_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        pelicula.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    try: 
        pelicula = Pelicula.objects.get(pk=pk) 
    except Pelicula.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def pelicula_list_published(request): 
    if request.method == 'GET': 
        pelicula_serializer = PeliculaSerializer(pelicula, many=True)
        return JsonResponse(pelicula_serializer.data, safe=False)
   

