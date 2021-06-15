from django.db import models

class Teams(models.Model):
    name = models.CharField(max_length=32)
    work = models.CharField(max_length=32)