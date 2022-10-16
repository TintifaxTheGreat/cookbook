from django.db.models import PositiveSmallIntegerField

from wagtail.core import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.core.fields import StreamField
from wagtail.core.blocks import ListBlock, RichTextBlock

choices = [
    ('EL', 'EL'),
    ('TL', 'TL'),
    ('g', 'g'),
    ('kg', 'kg'),
    ('ml', 'ml'),
    ('l', 'l'),
    ('Stk', 'Stk'),
    ('Prise', 'Prise'),
    ('Spritzer', 'Spritzer'),
]


class IngredientBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    amount = blocks.FloatBlock(
        label="Menge",
        help_text="Menge",
        required=False,
        min_value=0.0,
        max_value=999999.0,
    )
    unit = blocks.ChoiceBlock(
        label="Einheit",
        required=False,
        choices=choices,
    )

    class Meta:
        icon = "snippet"
        label = "Zutaten"


class SectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        label="Überschrift",
        required=False,
    )
    ingredients = ListBlock(
        IngredientBlock,
        label="Zutaten",
        required=True,
        icon="form",
    )
    instructions = RichTextBlock(
        label="Anweisungen",
        required=True,
    )

    class Meta:
        icon = "form"
        label = "Rezeptabschnitt"


class RecipePage(Page):
    portions = PositiveSmallIntegerField(
        blank=False,
        verbose_name="Portionen",
    )

    sections = StreamField([
        ('sections', SectionBlock()),
    ],
        use_json_field=False,
        blank=False,
        verbose_name="Rezeptabschnitte",
    )

    comments = RichTextField(
        blank=True,
        verbose_name="Kommentar",
    )

    search_fields = Page.search_fields + [
        index.SearchField('sections'),
        index.SearchField('comments'),
    ]

    content_panels = [
        FieldPanel('title', heading='Rezeptname'),
        FieldPanel('portions'),
        FieldPanel('sections'),
        FieldPanel('comments', ),
    ]

RecipePage._meta.get_field("title").help_text = None

class RecipeIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
