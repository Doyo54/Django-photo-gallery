from django.db import models
import datetime as dt

class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'image/',null =True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()


