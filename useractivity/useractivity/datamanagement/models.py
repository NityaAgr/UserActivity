from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.TextField(blank=False)
    url = models.TextField(blank=False)
