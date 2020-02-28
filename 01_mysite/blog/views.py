from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Artigo


def lista_de_artigos(request):
    artigos = Artigo.objects \
        .filter(data_publicacao__lte=timezone.now()) \
        .order_by('data_publicacao')
    return render(request, 'blog/artigos.html', {'artigos': artigos})


def artigo_detalhe(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'blog/artigo_detalhe.html', {'artigo': artigo})
