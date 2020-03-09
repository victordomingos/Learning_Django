import datetime

from django.db import models
from django.utils import timezone


class Questao(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('date_published')

    def __str__(self):
        return self.texto

    def foi_publicada_recentemente(self):
        agora = timezone.now()
        return agora - datetime.timedelta(days=1) <= self.data_publicacao <= agora


class Escolha(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto
