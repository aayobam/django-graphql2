from django.db import models
from django.urls import reverse
from apps.common.models import TimeStampsModel



class Category(TimeStampsModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('-created_on',)
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"category_id":self.id})