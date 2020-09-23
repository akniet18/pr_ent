# Generated by Django 3.0.8 on 2020-09-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_course', '0003_onlinecourse_type_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecourse',
            name='type_cours',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'ENT'), (2, 'НЗМ/ФМ/КТЛ'), (3, 'English')], null=True),
        ),
    ]
