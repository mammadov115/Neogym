from app.models import SectionImages

def hero_section_bg_image(request):
    hsbg_image = SectionImages.objects.first().hero_section.url
    return locals()