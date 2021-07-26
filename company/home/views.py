from django.shortcuts import render
from .models import Slider

# Create your views here.
def home(request):
    obj = Slider.objects.all()
    context = {'obj':obj}
    return render(request, 'home/home.html', context )
