# Generated by Django 3.0.8 on 2020-08-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
