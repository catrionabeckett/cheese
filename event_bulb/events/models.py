from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

# Create your models here.
