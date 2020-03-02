from django.urls import path

from . import views

urlpatterns = [
    path('rascunhos/', views.rascunhos, name='rascunhos'),
    path('', views.artigos, name='artigos'),
    path('artigo/<int:pk>/', views.artigo_detalhe, name='artigo_detalhe'),
    path('artigo/<int:pk>/publicar', views.artigo_publicar, name='artigo_publicar'),
    path('artigo/<int:pk>/editar', views.artigo_editar, name='artigo_editar'),
    path('artigo/<int:pk>/eliminar', views.artigo_eliminar, name='artigo_eliminar'),
    path('artigo/novo/', views.artigo_novo, name='artigo_novo'),

]
