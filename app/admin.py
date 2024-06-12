from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import *
# Register your models here.

@admin.register(SectionImages)
class SectionImagesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        is_empty = SectionImages.objects.count() == 0
        return True if is_empty else False


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    ordering = ["pk"]


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    ordering = ['pk']


@admin.register(HealthySection)
class HealthySectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        is_empty = HealthySection.objects.count() == 0
        return True if is_empty else False


@admin.register(InfoSection)
class InfoSectionAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        if InfoSection.objects.count() == 0:
            return True
        
@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['name', "email", "sended_at"]


admin.site.register(TrainerSection)
