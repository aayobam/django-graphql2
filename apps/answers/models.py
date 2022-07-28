from django.urls import reverse
from django.db import models
from apps.questions.models import Question
from apps.common.models import TimeStampsModel
from django.utils.translation import gettext_lazy as _


class Answer(TimeStampsModel):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.answer_text

    def get_absolute_url(self):
        return reverse("answer_detail", kwargs={"answer_id":self.id})

