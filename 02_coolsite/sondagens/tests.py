import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Questao


class QuestaoModelTests(TestCase):
    def test_foi_publicada_recentemente_with_old_question(self):
        """ foi_publicada_recentemente() devolve False para questoes cuja data há mais de 1 dia """
        ontem = timezone.now() - datetime.timedelta(days=1)
        questao_antiga = Questao(data_publicacao=ontem)
        self.assertIs(questao_antiga.foi_publicada_recentemente(), False)

    def test_foi_publicada_recentemente_with_future_question(self):
        """ foi_publicada_recentemente() devolve False para questoes cuja data seja no futuro """
        daqui_a_um_mes = timezone.now() + datetime.timedelta(days=30)
        questao_futura = Questao(data_publicacao=daqui_a_um_mes)
        self.assertIs(questao_futura.foi_publicada_recentemente(), False)

    def test_foi_publicada_recentemente_with_recent_question(self):
        """ foi_publicada_recentemente() devolve True para questoes publciadas no último dia """
        ult_dia = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        questao_recente = Questao(data_publicacao=ult_dia)
        self.assertIs(questao_recente.foi_publicada_recentemente(), True)
