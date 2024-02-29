from django.db import models

# Create your models here.
class SectionImages(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=f"section-images/" ,max_length=150, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['id']


class Slider(models.Model):
    first_title = models.CharField(max_length=150)
    second_title = models.CharField(max_length=150)
    third_title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return f'{self.first_title} {self.second_title} {self.third_title}'
    

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

