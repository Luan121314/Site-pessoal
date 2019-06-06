from django.shortcuts import render
from .models import DadosContato

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'meusCursos.html')

def contato(request):
    return render(request, 'contato.html')

def saveContato(request):
    
    if request.method == 'POST':
        userNameSystemDado = request.user.username
        nameDado = request.POST['name']
        emailDado = request.POST['email']
        textoDado = request.POST['txtTextArea']
        new_DadosContato = DadosContato(nomeSis=userNameSystemDado, nome=nameDado, email=emailDado, texto=textoDado)
        new_DadosContato.save()
        dado = nameDado + ", sua menssagem foi enviada com sucesso"

    return render(request, 'contato.html', {'dadaRetornado': dado})