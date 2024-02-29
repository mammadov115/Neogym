from typing import Any
from django.core.management.base import BaseCommand, CommandError
from ...models import SectionImages

titles = [
    "Hero Section",
    "Us Section",
    "Healthy Section",
    "Trainer Section",
]


class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any):
        try:
            for title in titles:
                SectionImages.objects.get_or_create(title=title)   
            print("Objects successfully created.")
        except:
            raise CommandError("Some errors occured.")