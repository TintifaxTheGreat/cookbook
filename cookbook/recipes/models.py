from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class RecipeIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class RecipePage(Page):
    instructions = RichTextField(blank=True)
    comments = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('instructions'),
        index.SearchField('comments'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('instructions'),
        FieldPanel('comments'),
    ]