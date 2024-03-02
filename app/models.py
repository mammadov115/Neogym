from django.db import models

# Create your models here.
class SectionImages(models.Model):
    hero_section = models.ImageField("Hero Section", upload_to="SectionImages/HeroSection", null=True)
    us_section = models.ImageField("Us Section", upload_to="SectionImages/UsSection", null=True)
    healthy_section = models.ImageField("Healthy Section", upload_to="SectionImages/HeathySection", null=True)
    trainer_section = models.ImageField("Trainer Section", upload_to="SectionImages/TrainerSection", null=True)
    contact_section = models.ImageField(verbose_name="Contact Section", upload_to="SectionImages/ContactSection/", null=True)
    
    def __str__(self) -> str:
        return "Section Images"

    class Meta:
        ordering = ['id']
        verbose_name_plural= "Section Images"


class Slider(models.Model):
    first_title = models.CharField(max_length=150)
    second_title = models.CharField(max_length=150)
    third_title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return f'{self.first_title} {self.second_title} {self.third_title}'
    

class WhyChooseUs(models.Model):
    image = models.ImageField(upload_to="Why Choose Us Section/",null=True)
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Why Choose Us"
    

class HealthySection(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return "Healthy Section"
    

class TrainerSection(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="trainer-pictures/")
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    ig_link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name


class InfoSection(models.Model):
    location = models.CharField(max_length=250)
    phonr_number = models.CharField(max_length=20)
    email = models.EmailField()
    footer_text = models.TextField()

