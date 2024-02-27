from django.shortcuts import render
from .models import *
from textwrap import wrap

# Create your views here.
def home(request):
    slider = Slider.objects.all()
    return render(request, template_name="index.html", context=locals())

def why_us(request):
    return render(request, template_name="why.html")

def trainers(request):
    return render(request, template_name="trainer.html")

def contact_us(request):
    return render(request, template_name="contact.html")