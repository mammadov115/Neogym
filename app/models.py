from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

class HealthySection(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

class TrainerSection(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="trainer-pictures/")
    fb_link = models.URLField(null=True)
    tw_link = models.URLField(null=True)
    ig_link = models.URLField(null=True)


class ContactSection(models.Model):
    image = models.ImageField(upload_to="contact-section/")


class Messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=200)
    message = models.TextField()


class InfoSection(models.Model):
    location = models.CharField(max_length=250)
    phonr_number = models.CharField(max_length=20)
    email = models.EmailField()
    footer_text = models.TextField()

