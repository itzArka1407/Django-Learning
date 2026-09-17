from typing_extensions import override

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @override
    def __str__(self):
        return self.title
