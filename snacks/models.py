from django.db import models

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=40)
    isgood = models.BooleanField()