# pages/models.py
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    link = models.BooleanField(default=True)
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
