from unicodedata import category
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
    
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'image/',null =True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
     
    def delete_image(self):
        self.delete()

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__location=location).all()
        return image_location

    @classmethod
    def filter_by_category(cls, category):
        image_category = Image.objects.filter(category__category=category).all()
        return image_category

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images


