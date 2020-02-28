from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_de_artigos, name='artigos'),
    path('artigo/<int:pk>/', views.artigo_detalhe, name='artigo_detalhe'),
]
