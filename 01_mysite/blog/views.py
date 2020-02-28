from django.shortcuts import render
from django.utils import timezone

from .models import Artigo


def lista_de_artigos(request):
    artigos = Artigo.objects \
        .filter(data_publicacao__lte=timezone.now()) \
        .order_by('data_publicacao')
    return render(request, 'blog/artigos.html', {'artigos': artigos})
