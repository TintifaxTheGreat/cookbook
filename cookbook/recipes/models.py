from django.db import models

from wagtail.core import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.core.fields import StreamField
from wagtail.core.blocks import StreamBlock


class SectionBlock(blocks.StreamBlock):
    ingredients = StreamBlock([
        ('name', blocks.TextBlock(
            help_text="Zutat",
            required=True,
        )),
        ('amount', blocks.FloatBlock(
            label="Menge",
            help_text="Menge",
            required=False,
            min_value=0.0,
            max_value=999999.0,
        )),
        ('unit', blocks.ChoiceBlock(
            label="Einheit",
            required=False,
            choices=[
                ('el', 'Esslöffel'),
                ('tl', 'Teelöffel'),
            ]
        )),
    ],
        use_json_field=False,
        blank=True,
    )

    instructions = RichTextField(blank=True)

    class Meta:
        icon = "form"
        label = "Rezeptabschnitt hinzufügen"


class RecipePage(Page):
    sections = StreamField([
        ('sections', SectionBlock()),
    ],
        use_json_field=False,
        blank=False,
    )

    comments = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('sections'),
        index.SearchField('comments'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('sections'),
        FieldPanel('comments'),
    ]


class RecipeIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
