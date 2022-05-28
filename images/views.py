from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def home(request):
    image = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'image.html', {"image":image, 'locations': locations})
# Create your views here.
def index(request):
    return render(request, 'index.html')

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})

def image_category(request, category):
    images = Image.filter_by_category(category)
    print(images)
    return render(request, 'location.html', {'location_images': images})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search_results.html', {"message": message})
