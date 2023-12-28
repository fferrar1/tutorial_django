from django.contrib import admin

from .models import Choice, Question


class ChoiceInLine(admin.TabularInline): #tabular vai apresentar os campos em forma de tabela, o stacked vai criar um formulário para cada choice
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin) #disponibiliza a Question criada na página do admin