from django.db import models
from django.urls import reverse
from apps.quizzes.models import Quiz
from apps.common.models import TimeStampsModel
from django.utils.translation import gettext_lazy as _



class Question(TimeStampsModel):
    SCALE = (
        (0, _("Fundamental1")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert"))
    )

    TYPE = (
        (0, _("Multiple Choice")),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0)
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField(choices=SCALE)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_on",)
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"question_id":self.id})
