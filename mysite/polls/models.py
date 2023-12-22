from django.db import models
#o exemplo escolhido usa um app de enquetes, por isso temos Question, com a pergunta e a data de publicação; e Choice, com a "resposta" e o totalizador de conta dos votos
class Question(models.Modrel):
    question_text = models.CharField(max_length=200) #charfield informa que o campo selecionado é do tipo char
    pub_date = models.DateTimeField("date published") #datetimefield informa ao banco de dados que o campo selecionado é do tipo datetime

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) #max_length é utilizado tanto no banco de dados quanto na futura validação
    votes = models.IntegerField(default=0) #campo votes tipo Integer