import csv
from django.core.management.base import BaseCommand
from wagtail.core.models import Page
from recipes.models import RecipeIndexPage, RecipePage


class Command(BaseCommand):
    help = "Experimental import"

    def handle(self, *args, **options):
        home = Page.objects.get(id=10)



        reader = csv.DictReader(open("../data/gourmet_export.csv"), delimiter='|', quotechar='"')
        for row in reader:
            recipe_page = RecipePage(
                
            )


            home.add_child(instance=RecipePage)

            title = row["title"]
            print(title)

