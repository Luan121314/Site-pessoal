from django.shortcuts import render
from sitePessoalApp.models import DadosContato

# Create your views here.
def index2(request):
    dado = DadosContato.objects.all()
    return render(request, 'index2.html',{'dado': dado})


