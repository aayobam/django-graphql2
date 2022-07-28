from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


class TimeStampsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name = _("Object Identifier"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name = _("Date Created"))
    updated_on = models.DateTimeField(auto_now=True, verbose_name = _("Date Updated"))

    class Meta:
        abstract = True