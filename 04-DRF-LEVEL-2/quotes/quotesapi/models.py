from django.db import models

# Create your models here.


class Quote(models.Model):
    quote_author = models.CharField(max_length=255)
    quote_body = models.TextField()
    context = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
