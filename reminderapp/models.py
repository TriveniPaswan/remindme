from django.contrib.auth.models import User
from django.db import models

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    priority = models.CharField(max_length=20, default="Medium")
    def __str__(self):
        return f"{self.date} {self.time} - {self.message[:20]}"
