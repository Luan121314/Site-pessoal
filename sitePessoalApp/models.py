from django.db import models

from django.utils import timezone

# Create your models here.(

class DadosContato(models.Model):
    def __str__(self):
        return self.nome
    nomeSis = models.CharField(max_length=20, default= 'desconhecido')
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    texto = models.CharField(max_length=300)
    data = models.DateTimeField(
            default=timezone.now)

