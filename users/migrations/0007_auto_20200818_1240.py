# Generated by Django 3.0.8 on 2020-08-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uin',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
    ]
