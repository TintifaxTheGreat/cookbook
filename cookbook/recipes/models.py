from django.db.models import PositiveSmallIntegerField, CASCADE
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel, TitleFieldPanel
from wagtail.blocks import ListBlock, RichTextBlock, StructBlock, CharBlock, FloatBlock, ChoiceBlock
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

choices = [
    ('EL', 'EL'),
    ('TL', 'TL'),
    ('g', 'g'),
    ('kg', 'kg'),
    ('ml', 'ml'),
    ('l', 'l'),
    ('Stk', 'Stk'),
    ('Prise', 'Prise'),
    ('Pkg', 'Pkg'),
    ('Bund', 'Bund'),
    ('Spritzer', 'Spritzer'),
    ('Tropfen', 'Tropfen'),
]


class IngredientBlock(StructBlock):
    name = CharBlock()
    amount = FloatBlock(
        label="Menge",
        help_text="Menge",
        required=False,
        min_value=0.0,
        max_value=999999.0,
    )
    unit = ChoiceBlock(
        label="Einheit",
        required=False,
        choices=choices,
    )

    class Meta:
        icon = "snippet"
        label = "Zutaten"


class SectionBlock(StructBlock):
    heading = CharBlock(
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


class RecipePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'RecipePage', on_delete=CASCADE, related_name='tagged_items')


class RecipePage(Page):
    portions = PositiveSmallIntegerField(
        blank=False,
        verbose_name="Portionen",
    )

    sections = StreamField([
        ('sections', SectionBlock()),
    ],
        use_json_field=True,
        blank=False,
        verbose_name="Rezeptabschnitte",
    )

    comments = RichTextField(
        null=True,
        blank=True,
        verbose_name="Kommentar",
    )

    source = RichTextField(
        null=True,
        blank=True,
        verbose_name="Quelle",
    )

    tags = ClusterTaggableManager(through=RecipePageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('sections'),
        index.SearchField('comments'),
        index.SearchField('source'),
    ]

    content_panels = [
        TitleFieldPanel('title', placeholder="Rezeptname", heading='Rezeptname'),
        FieldPanel('portions'),
        FieldPanel('sections'),
        FieldPanel('tags'),
        FieldPanel('comments'),
        FieldPanel('source'),
    ]

    @staticmethod
    def get_all_tags():
        tags = RecipePage.tags.most_common()
        return tags


RecipePage._meta.get_field("title").help_text = None


class RecipeIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        children_sorted = RecipePage.objects.child_of(RecipeIndexPage.objects.first()).live().order_by(
            'title')

        tag = request.GET.get('tag')
        if tag:
            children_sorted = children_sorted.filter(tags__name=tag)

        context['children_sorted_count'] = children_sorted.count()
        paginator = Paginator(children_sorted, 10)
        children_sorted = paginator.page(1)
        context['children_sorted'] = children_sorted
        context['page_next'] = 2
        return context
