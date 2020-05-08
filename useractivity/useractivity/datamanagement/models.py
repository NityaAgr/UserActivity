from django.db import models

# Models created here with the required fiels.

# User model

class User(models.Model):
    id = models.TextField( primary_key=True)
    real_name = models.TextField(blank=False)
    tz = models.TextField(blank=False)
    
# primary_key defined that the coulumn walue should be unique in table.

# User Activity model

class UserActivity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_time = models.TextField(blank=False)
    end_time = models.TextField(blank=False)

