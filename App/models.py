from django.db import models

# Create your models here.
class Resturant(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=30)
    ort = models.CharField(max_length=30)
    url = models.CharField(max_length=30)