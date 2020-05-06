from django.db import models

# Create your models here.


class User(models.Model):
    id = models.TextField( primary_key=True)
    real_name = models.TextField(blank=False)
    tz = models.TextField(blank=False)
    

class UserActivity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_time = models.TextField(blank=False)
    end_time = models.TextField(blank=False)