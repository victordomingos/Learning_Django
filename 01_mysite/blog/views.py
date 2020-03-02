from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import ArtigoForm
from .models import Artigo


def artigos(request):
    artigos = Artigo.objects \
        .filter(data_publicacao__lte=timezone.now()) \
        .order_by('-data_publicacao')
    return render(request, 'blog/artigos.html', {'artigos': artigos})


def rascunhos(request):
    artigos = Artigo.objects \
        .filter(data_publicacao__isnull=True) \
        .order_by('data_criacao')
    return render(request, 'blog/rascunhos.html', {'artigos': artigos})


def artigo_detalhe(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'blog/artigo_detalhe.html', {'artigo': artigo})


def artigo_publicar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigo.publicar()
    return redirect('artigo_detalhe', pk=pk)


def artigo_eliminar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigo.delete()
    return redirect('artigos')


def artigo_novo(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        if form.is_valid():
            # commit=False -> não guardar já, pq ainda queremos especificar o autor etc.
            artigo = form.save(commit=False)
            artigo.autor = request.user
            # Agora sim, já podemos guardar.
            artigo.save()
            return redirect('artigo_detalhe', pk=artigo.pk)
    else:
        form = ArtigoForm()

    return render(request, 'blog/artigo_edit.html', {'form': form})


def artigo_editar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigo_detalhe', pk=artigo.pk)
    else:
        form = ArtigoForm(instance=artigo)

    return render(request, 'blog/artigo_edit.html', {'form': form})
