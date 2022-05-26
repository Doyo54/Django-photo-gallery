from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    image = Image.objects.all()
    return render(request, 'image.html', {"image":image})
# Create your views here.
def index(request):
    return render(request,'index.html')
