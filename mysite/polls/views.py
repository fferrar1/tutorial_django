from django.http import HttpResponse #criando a view mais simples 

def index (request):
    return HttpResponse("Primeiro teste de polls em Django")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)