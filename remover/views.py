from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rembg.bg import remove
from PIL import Image
from django.conf import settings  # Import the settings module
import random
import os

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def store(request):
    if request.method == 'POST' and request.FILES.get('image'):
        file_name = str(random.random()).encode('utf-8')
        file = request.FILES['image']
        
        img = Image.open(file)
        result = remove(img)

        # Construct the path to the image file using settings.STATIC_ROOT
        file_path = os.path.join(settings.STATIC_ROOT, 'images', file_name + '.png')
        result.save(file_path)
        
        # Return the image URL
        image_url = os.path.join('images', file_name + '.png')
        return render(request, 'image.html', {'image': image_url})
        
        # redirect to image
        return HttpResponse(file_name + '.png')
    
    return render(request, 'index.html')
