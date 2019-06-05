from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'meusCursos.html')

def contato(request):
    return render(request, 'contato.html')