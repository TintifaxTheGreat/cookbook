# Generated by Django 4.1.2 on 2022-10-15 14:41

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_remove_recipepage_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepage',
            name='sections',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StreamBlock([]))], use_json_field=False),
        ),
    ]
