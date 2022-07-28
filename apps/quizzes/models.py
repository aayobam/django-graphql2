from django.db import models
from django.urls import reverse
from apps.common.models import TimeStampsModel
from apps.categories.models import Category
from django.utils.translation import gettext_lazy as _


class Quiz(TimeStampsModel):
    title = models.CharField(max_length=255, default=_("New Quiz"))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-created_on',)
        verbose_name = "Quiz"
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("quiz_detail", kwargs={"quiz_id":self.id})
