from django.db import models
from django.utils.translation import ugettext_lazy as _


def tutor_photos_dir(instanse, filename):
    usrnme = f'{instanse.full_name}'
    folder_name = f"{usrnme}/{filename}"
    return folder_name

class OnlineCourse(models.Model):
    TYPE_ENT = 1
    TYPE_NZM = 2
    TYPE_ENGLISH = 3
    TYPE_COURSES = (
        (TYPE_ENT, _('ENT')),
        (TYPE_NZM, _('НЗМ/ФМ/КТЛ')),
        (TYPE_ENGLISH, _('English')),
    )

    type_cours = models.SmallIntegerField(blank=True, null=True, choices=TYPE_COURSES)
    full_name = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to=tutor_photos_dir, default="default/default.png")
    subject_name = models.CharField(max_length=150)
    education = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=250, blank=True, null=True)

    about = models.TextField(blank=True, null=True)
    card = models.CharField(max_length=150)
    price = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.full_name + " - " + self.subject_name