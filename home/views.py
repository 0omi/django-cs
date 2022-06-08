from django.shortcuts import render
from .models import Photo
# Create your views here.
def home(request):
    return render (request, 'home/home.html', {'pho':Photo.objects.all()} ) # pho is the value of all images in the database


