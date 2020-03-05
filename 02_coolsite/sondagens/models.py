from django.db import models


class Questao(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('date_published')


class Escolha(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
