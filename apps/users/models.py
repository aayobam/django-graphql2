from django.urls import reverse
from django.db import models
from .managers import CustomUserManager
from apps.common.models import TimeStampsModel
from django.contrib.auth.models import AbstractUser, AbstractBaseUser



class CustomUser(TimeStampsModel, AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"user_id": self.id})
