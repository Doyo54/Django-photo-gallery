from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def home(request):
    image = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'image.html', {"image":image, 'locations': locations})
# Create your views here.

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})

def image_category(request, category):
    images = Image.filter_by_category(category)
    print(images)
    return render(request, 'location.html', {'location_images': images})
