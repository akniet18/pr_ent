# Generated by Django 3.0.8 on 2020-09-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200819_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]