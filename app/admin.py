from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ["separated_title"]
    
admin.site.register(WhyChooseUs)
admin.site.register(HealthySection)
admin.site.register(TrainerSection)
admin.site.register(ContactSection)
admin.site.register(Messages)
admin.site.register(InfoSection)