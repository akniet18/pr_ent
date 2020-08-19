from django.db import models


class OnlineCourse(models.Model):
    full_name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=150)
    card = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name + " - " + self.subject_name