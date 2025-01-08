from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):
    STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description =  models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default= 'pending')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"