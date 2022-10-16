# Generated by Django 4.1.2 on 2022-10-16 10:18

from django.db import migrations
import recipes.models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_alter_recipepage_sections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepage',
            name='sections',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Überschrift', required=False)), ('instructions', wagtail.blocks.RichTextBlock(label='Anweisungen', required=True)), ('ingredients', wagtail.blocks.ListBlock(recipes.models.IngredientBlock))]))], use_json_field=False),
        ),
    ]
