from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Questao, Escolha


class IndexView(generic.ListView):
    template_name = 'sondagens/index.html'
    context_object_name = 'ultimas_questoes'

    def get_queryset(self):
        """ Devolve as últimas 5 questões publicadas"""
        return Questao.objects.order_by('-data_publicacao')[:5]


class DetailView(generic.DetailView):
    model = Questao
    template_name = 'sondagens/detalhe.html'


class ResultsView(generic.DetailView):
    model = Questao
    template_name = 'sondagens/resultados.html'


def votar(request, question_id):
    """ Página que é mostrada ao registar um voto """
    questao = get_object_or_404(Questao, pk=question_id)
    try:
        escolha_selecionada = questao.escolha_set.get(pk=request.POST['escolha'])
    except (KeyError, Escolha.DoesNotExist):
        context = {'questao': questao,
                   'mensagem_de_erro': 'Não selecionou uma questão.'
                   }
        return render(request, 'sondagens/detalhe.html', context)
    else:
        escolha_selecionada.votos = F('votos') + 1
        escolha_selecionada.save()
        return HttpResponseRedirect(reverse('sondagens:resultados',
                                            args=(questao.id,)))
