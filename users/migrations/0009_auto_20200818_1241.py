# Generated by Django 3.0.8 on 2020-08-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200818_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uin',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
