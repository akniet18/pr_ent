from django.db import models
from datetime import datetime


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

def test_photos_dir(instance, filename):
    folder_name = f'{instance.question.id}/{filename}'
    return folder_name

class TestPhoto(models.Model):
    photo = models.ImageField(upload_to=test_photos_dir)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="question_photo", null=True)

    def __str__(self):
        return self.question.text


class question_variant(models.Model):
    text = models.TextField()
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="question_variant", null=True)

    def __str__(self):
        return self.text

class Question(models.Model):
    text = models.TextField()
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="test_subject")

    def __str__(self):
        return self.text

    
    def count_variant(self):
        al = self.question_variant.all()
        return len(al)



class FeedBack(models.Model):
    text = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text