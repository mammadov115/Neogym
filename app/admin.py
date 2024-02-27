from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(SectionImages)
class SectionImagesAdmin(admin.ModelAdmin):
    readonly_fields = ["title"]
    list_display = ["title"]



admin.site.register(Slider)
admin.site.register(WhyChooseUs)
admin.site.register(HealthySection)
admin.site.register(TrainerSection)
admin.site.register(ContactSection)
admin.site.register(Messages)
admin.site.register(InfoSection)