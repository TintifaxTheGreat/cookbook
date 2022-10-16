# Generated by Django 4.1.2 on 2022-10-16 09:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_alter_recipepage_sections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepage',
            name='sections',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StreamBlock([('instructions', wagtail.blocks.RichTextBlock(label='Anweisungen', required=True)), ('ingredients', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('amount', wagtail.blocks.FloatBlock(help_text='Menge', label='Menge', max_value=999999.0, min_value=0.0, required=False)), ('unit', wagtail.blocks.ChoiceBlock(choices=[('el', 'Esslöffel'), ('tl', 'Teelöffel')], label='Einheit', required=False))], label='Zutaten', required=True))]))], use_json_field=False),
        ),
    ]
