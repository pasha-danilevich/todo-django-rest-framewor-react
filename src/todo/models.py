from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length = 100,
        blank = False,
    )
    completed = models.BooleanField(
        default = False,
        blank = True,
        null = True
    )

    def __str__(self) -> str:
        return self.title