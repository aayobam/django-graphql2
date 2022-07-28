from django.contrib import admin
from .models import Question


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'technique', 'title', 'is_active')
