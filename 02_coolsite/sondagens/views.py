from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questao, Escolha


def index(request):
    """ Lista ou índice de questões """
    ultimas_questoes = Questao.objects.order_by('data_publicacao')[:5]
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'sondagens/index.html', context)


def detalhe(request, question_id):
    """ Página que será mostrada ao abrir uma questão da lista """
    questao = get_object_or_404(Questao, pk=question_id)
    return render(request, 'sondagens/detalhe.html', {'questao': questao})


def resultados(request, question_id):
    """ Resultados da votacao numa dada sondagem """
    questao = get_object_or_404(Questao, pk=question_id)
    return render(request, 'sondagens/resultados.html', {'questao': questao})


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
