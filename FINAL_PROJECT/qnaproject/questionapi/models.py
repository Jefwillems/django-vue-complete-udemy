from django.db import models
from profiles.models import UserProfile


class Question(models.Model):
    content = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Answer(models.Model):
    content = models.CharField(max_length=255)
