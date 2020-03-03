from django.urls import path

from . import views

urlpatterns = [
    path('', views.artigos, name='artigos'),
    path('rascunhos/', views.rascunhos, name='rascunhos'),
    path('artigo/<int:pk>/', views.artigo_detalhe, name='artigo_detalhe'),
    path('artigo/<int:pk>/publicar', views.artigo_publicar, name='artigo_publicar'),
    path('artigo/<int:pk>/editar', views.artigo_editar, name='artigo_editar'),
    path('artigo/<int:pk>/eliminar', views.artigo_eliminar, name='artigo_eliminar'),
    path('artigo/<int:pk>/comentar', views.adicionar_comentario, name='adicionar_comentario'),
    path('comentario/<int:pk>/eliminar', views.eliminar_comentario, name='eliminar_comentario'),
    path('comentario/<int:pk>/aprovar', views.aprovar_comentario, name='aprovar_comentario'),
    path('artigo/novo/', views.artigo_novo, name='artigo_novo'),

]
