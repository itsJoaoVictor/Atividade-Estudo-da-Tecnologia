from django.db import models

class Usuario(models.Model):
    cpf = models.IntegerField()
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
