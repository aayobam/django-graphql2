from django.contrib import admin
from .models import Answer


@admin.register(Answer)
class AdminAnser(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer_text', 'is_right')