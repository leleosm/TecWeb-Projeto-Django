from django.db import models
from django.utils import timezone

class NovoAluno(models.Model):
    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    sexo = models.CharField("Sexo", max_length=100)
    email = models.EmailField("E-mail", max_length=100)
    telefone = models.IntegerField("Telefone")
    endereco = models.CharField("Endereço", max_length=100)
    cep = models.IntegerField("CEP")
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=100)
    curso = models.CharField("Curso", max_length=100)

    def __str__(self):
        return self.nome    