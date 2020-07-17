from django.db import models
from datetime import datetime


class test_variant(models.Model):
    variant = models.CharField(max_length=50)

    def __str__(self):
        return self.variant


class Subject(models.Model):
    name = models.CharField(max_length=50)
    variant = models.ForeignKey("test_variant", on_delete=models.CASCADE, related_name="variant_test", null=True)

    def __str__(self):
        return self.name
    

def test_photos_dir(instanse, filename):
    usrnme = f'{instanse.test.id}'
    folder_name = f'{instance.test.subject.name}/{usrnme}/{filename}'
    return folder_name

class TestPhoto(models.Model):
    photo = models.ImageField(upload_to=test_photos_dir)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="question_photo", null=True)

    def __str__(self):
        return self.question.question


class question_variant(models.Model):
    text = models.TextField()
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="question_variant", null=True)

    def __str__(self):
        return self.text

class Question(models.Model):
    question = models.TextField()
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="test_subject")

    def __str__(self):
        return self.question
