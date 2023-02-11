from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30) # change to 30
    completed = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.task}'
