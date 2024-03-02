from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        print(request)
        if form.is_valid():
            form.save()
            messages.success(request, "Message successfully sended.")



    slider = Slider.objects.all()
    section_images = SectionImages.objects.first()
    wcu_section = WhyChooseUs.objects.all()
    h_section = HealthySection.objects.first()
    trainers = TrainerSection.objects.all()
    form = MessageForm()
    return render(request, template_name="index.html", context=locals())
 
def why_us(request):
    return render(request, template_name="why.html")

def trainers(request):
    return render(request, template_name="trainer.html")

def contact_us(request):
    return render(request, template_name="contact.html")