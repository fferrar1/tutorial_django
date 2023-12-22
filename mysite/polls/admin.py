from django.contrib import admin

from .models import Question

admin.site.register(Question) #disponibiliza a Question criada na página do admin
