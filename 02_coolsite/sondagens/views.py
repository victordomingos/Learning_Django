from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Questao


def index(request):
    ultimas_questoes = Questao.objects.order_by('data_publicacao')[:5]
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'sondagens/index.html', context)


def detalhe(request, question_id):
    questao = get_object_or_404(Questao, pk=question_id)
    return render(request, 'sondagens/detalhe.html', {'questao': questao})


def resultados(request, question_id):
    return HttpResponse(f"Está a visualizar os resultados da questão {question_id}.")


def votar(request, question_id):
    return HttpResponse(f"Está a votar na questão {question_id}.")
