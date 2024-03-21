from typing import Any
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import RedirectView
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message successfully sended.")
            return redirect("redirect")
    
    slider = Slider.objects.all()
    section_images = SectionImages.objects.first()
    wcu_section = WhyChooseUs.objects.all()
    h_section = HealthySection.objects.first()
    trainers = TrainerSection.objects.all()
    form = MessageForm()
    return render(request, template_name="index.html", context=locals())
 
def why_us(request):
    wcu_section = WhyChooseUs.objects.all()
    return render(request, template_name="why.html", context=locals())

def trainers(request):
    trainers = TrainerSection.objects.all()

    return render(request, template_name="trainer.html", context=locals())

def contact_us(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message successfully sended.")
            return render(request, template_name="contact.html", context=locals())

    form = MessageForm()
    return render(request, template_name="contact.html", context=locals())


class ViewMessageRedirectView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        return reverse("home") + "#contact"