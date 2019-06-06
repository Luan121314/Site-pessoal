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
    dado = auth.User
    nome = request.POST['name']
    email = request.POST['email']
    texto = request.POST['txtTextArea']
    new_DadosContato = DadosContato(nome=nome, email=email, texto=texto, author= default)
    
    # new_DadosContato.save()

    dado = "Salvo !"

    return render(request, 'contato.html', {'dadaRetornado': dado
    })