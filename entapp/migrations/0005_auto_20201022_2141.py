# Generated by Django 3.0.8 on 2020-10-22 15:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entapp', '0004_auto_20201022_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
