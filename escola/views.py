from django.shortcuts import render
from django.http import JsonResponse
from escola.models import Estudante, Curso
from escola.serializer import EstudanteSerializer, CursoSerializer
from rest_framework import viewsets

# Create your views here.

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'Marcos'
        }
        return JsonResponse(estudante)
    
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer