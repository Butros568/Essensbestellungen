from django.db import models

# Create your models here.
class Resturant(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=30)
    ort = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    

class Benutzer(models.Model):
    mail = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Items(models.Model):
    id = models.ImageField()
    preis = models.IntegerField()
    bezahlt = models.BooleanField()
    benutzer = models.ForeignKey(Benutzer)
    gericht = models.CharField(max_length=30)


class Bestellungen(models.Model):
    id = models.IntegerField()
    benutzer = models.ForeignKey(Benutzer)
    items = models.ForeignKey(Benutzer)
