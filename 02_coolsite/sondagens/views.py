from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Bem-vindo(a) à página inicial da aplicação web Sondagens!")

