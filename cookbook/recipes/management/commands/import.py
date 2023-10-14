import csv
import json
import math
from django.core.management.base import BaseCommand
from wagtail.models import Page
from recipes.models import RecipePage


class Command(BaseCommand):
    help = "Experimental import"

    def handle(self, *args, **options):
        home = Page.objects.get(id=10)

        ingredients = []
        oldtitle = ""
        recipe_page = RecipePage()

        start = True

        reader = csv.DictReader(
            open("../data/gourmet_export.csv"), delimiter='|', quotechar='"')
        for row in reader:
            if start or (row["title"] == oldtitle):
                if start:
                    oldtitle = row["title"]
                    start = False

                ingredients.append(
                    {
                        'name': row["item"],
                        'amount': row["amount"],
                        'unit': row["unit"],
                    }
                )

                section1 = {
                    'heading': "",
                    'ingredients': ingredients,
                    'instructions': row["instructions"],
                }

                recipe_page = RecipePage(
                    title=row["title"],
                    portions=math.floor(float(row["yields"])),
                    sections=json.dumps([
                        {
                            'type': "sections",
                            'value': section1
                        },
                    ]),
                    comments=row["modifications"],
                    source=row["link"],
                )

            else:
                oldtitle = row["title"]

                try:
                    home.add_child(instance=recipe_page)
                    recipe_page.save_revision().publish()
                except:
                    pass

                amount = 0
                try:
                    amount = math.floor(float(row["amount"]))
                except:
                    pass

                ingredients = [(
                    {
                        'name': row["item"],
                        'amount': amount,
                        'unit': row["unit"],
                    }
                )]
