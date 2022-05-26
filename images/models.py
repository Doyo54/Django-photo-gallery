from unicodedata import category
from django.db import models
import datetime as dt

class Category(models.Model):
    category = models.CharField(max_length=30)


class Location(models.Model):
    location = models.CharField(max_length=30)

class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'image/',null =True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

