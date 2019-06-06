from django.db import models
from django.utils import timezone

# Create your models here.(

class DadosContato(models.Model):
    def __str__(self):
        return self.texto

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    texto = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)

