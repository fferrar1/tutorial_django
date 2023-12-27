from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), #ex /polls/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), #ex /polls/5/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), #ex /polls/5/results
    path("<int:question_id>/vote/", views.vote, name="vote"), # ex /polls/5/vote
]
#o argumento de path:name é um poderoso aliado na hora de renomear urls;  path:view => Quando o Django encontra uma descrição que combina, chama a função view especificada com um objeto HttpRequest como primeiro argumento e qualquer valor “capturado” da rota como argumentos keyword.
