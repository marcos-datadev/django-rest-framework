from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'Marcos'
        }
        return JsonResponse(estudante)