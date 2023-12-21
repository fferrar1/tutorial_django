from django.http import HttpResponse #criando a view mais simples 

def index (request):
    return HttpResponse("Primeiro teste de polls em Django")
