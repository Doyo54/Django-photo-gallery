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

