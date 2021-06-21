from typing import Text
from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    reminder = models.BooleanField()
    
    def __str__(self):
        return self.text
     
