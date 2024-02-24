from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("why-us/", views.why_us, name="why-us"),
    path("trainers", views.trainers, name="trainers"),
    path("contact-us", views.contact_us, name="contact-us"),
    path("api/", include("api.urls"))
]
