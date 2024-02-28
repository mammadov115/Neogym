from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(SectionImages)
class SectionImagesAdmin(admin.ModelAdmin):
    fields = ["image"]
    list_display = ["title"]

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Slider)
admin.site.register(WhyChooseUs)
admin.site.register(HealthySection)
admin.site.register(TrainerSection)
admin.site.register(ContactSection)
admin.site.register(Messages)
admin.site.register(InfoSection)