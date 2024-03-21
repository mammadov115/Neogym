from app.models import SectionImages, InfoSection

def hero_section_bg_image(request):
    hsbg_image = SectionImages.objects.first().hero_section.url
    info_section = InfoSection.objects.first()
    section_images = SectionImages.objects.first()


    return locals()