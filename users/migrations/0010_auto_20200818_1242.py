# Generated by Django 3.0.8 on 2020-08-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200818_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uin',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]