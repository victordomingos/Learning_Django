from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import ArtigoForm
from .models import Artigo


def artigos(request):
    """ Lista de artigos (página principal) """
    lista_artigos = Artigo.objects \
        .filter(data_publicacao__lte=timezone.now()) \
        .order_by('-data_publicacao')
    return render(request, 'blog/artigos.html', {'artigos': lista_artigos})

@login_required()
def rascunhos(request):
    """ Lista de rascunhos de artigos """
    lista_rascunhos = Artigo.objects \
        .filter(data_publicacao__isnull=True) \
        .order_by('data_criacao')
    return render(request, 'blog/rascunhos.html', {'artigos': lista_rascunhos})


def artigo_detalhe(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'blog/artigo_detalhe.html', {'artigo': artigo})


@login_required
def artigo_publicar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigo.publicar()
    return redirect('artigo_detalhe', pk=pk)

@login_required()
def artigo_eliminar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigo.delete()
    return redirect('artigos')

@login_required()
def artigo_novo(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        if form.is_valid():
            # commit=False -> não guardar já, pq ainda queremos especificar autor etc.
            artigo = form.save(commit=False)
            artigo.autor = request.user
            # Agora sim, já podemos guardar.
            artigo.save()
            return redirect('artigo_detalhe', pk=artigo.pk)
    else:
        form = ArtigoForm()

    return render(request, 'blog/artigo_edit.html', {'form': form})

@login_required()
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
