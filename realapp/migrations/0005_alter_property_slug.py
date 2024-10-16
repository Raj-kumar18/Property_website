# Generated by Django 4.2.5 on 2023-09-23 10:03

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0004_alter_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title'),
        ),
    ]
