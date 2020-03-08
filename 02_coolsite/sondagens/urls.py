from django.urls import path

from . import views

app_name = 'sondagens'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detalhe, name='detalhe'),
    path('<int:question_id>/resultados/', views.resultados, name='resultados'),
    path('<int:question_id>/votar/', views.votar, name='votar'),
]
