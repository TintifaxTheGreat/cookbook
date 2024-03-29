# Generated by Django 4.2.5 on 2023-10-01 12:47

from django.db import migrations
import recipes.models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_recipepagetag_recipepage_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepage',
            name='sections',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Überschrift', required=False)), ('ingredients', wagtail.blocks.ListBlock(recipes.models.IngredientBlock, icon='form', label='Zutaten', required=True)), ('instructions', wagtail.blocks.RichTextBlock(label='Anweisungen', required=True))]))], use_json_field=True, verbose_name='Rezeptabschnitte'),
        ),
    ]
