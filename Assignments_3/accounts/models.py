from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="image/", blank=True)
    introduction = models.TextField(blank=True)
