from django.conf import settings
from django.db import models
from django.utils import timezone


class Artigo(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def comentarios_aprovados(self):
        return self.comentarios.filter(is_approved=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey('blog.Artigo',
                               on_delete=models.CASCADE,
                               related_name='comentarios')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def aprovar(self):
        self.is_approved = True
        self.save()

    def __str__(self):
        return self.texto
