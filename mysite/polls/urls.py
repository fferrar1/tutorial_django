from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
#o argumento de path:name é um poderoso aliado na hora de renomear urls;  path:view => Quando o Django encontra uma descrição que combina, chama a função view especificada com um objeto HttpRequest como primeiro argumento e qualquer valor “capturado” da rota como argumentos keyword.