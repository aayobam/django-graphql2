from django.contrib import admin
from .models import Quiz


@admin.register(Quiz)
class AdminQuiz(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_on', 'updated_on')