from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.username}'
