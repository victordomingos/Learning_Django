from django.urls import path

from . import views

app_name = 'sondagens'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detalhe'),
    path('<int:pk>/resultados/', views.ResultsView.as_view(), name='resultados'),
    path('<int:question_id>/votar/', views.votar, name='votar'),
]
