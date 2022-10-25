import csv
import json
from django.core.management.base import BaseCommand
from wagtail.core.models import Page
from recipes.models import RecipeIndexPage, RecipePage


class Command(BaseCommand):
    help = "Experimental import"

    def handle(self, *args, **options):
        home = Page.objects.get(id=10)

        ingredients = []
        oldtitle = ""

        reader = csv.DictReader(open("../data/gourmet_export.csv"), delimiter='|', quotechar='"')
        for row in reader:
            if row["title"] == oldtitle:
                ingredients.append(
                    {
                        'name': row["item"],
                        'amount': row["amount"],
                        'unit': row["unit"],
                    }
                )

            else:
                oldtitle = row["title"]

                section1 = {
                    'heading': "",
                    'ingredients': ingredients,
                    'instructions': "mytext",
                }

                recipe_page = RecipePage(
                    title=row["title"],
                    portions=4,  # TODO change this
                    sections=json.dumps([
                        {
                            'type': "sections",
                            'value': section1
                        },
                    ]),
                    comments=row["modifications"]
                )

                print(ingredients)

                #home.add_child(instance=recipe_page)
                #recipe_page.save_revision().publish()
