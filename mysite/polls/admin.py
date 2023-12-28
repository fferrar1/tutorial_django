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
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"] #cria um filtro
    search_fields = ["question_text"] #cria uma barra de pesquisa

admin.site.register(Question, QuestionAdmin) #disponibiliza a Question criada na página do admin