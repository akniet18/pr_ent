from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class SubjectSer(serializers.ModelSerializer):
    class Meta:
        model = Subject()
        fields = "__all__"

class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = TestPhoto()
        fields = "__all__"

class VariantSer(serializers.ModelSerializer):
    class Meta:
        model = question_variant()
        fields = "__all__"

class TestSer(serializers.ModelSerializer):
    question_variant = VariantSer(many=True)
    question_photo = PhotoSer(many=True)
    class Meta:
        model = Question()
        fields = "__all__"


class AnswerOneSer(serializers.Serializer):
    test_id = serializers.CharField()
    answer_id = serializers.CharField()


class passEntSer(serializers.Serializer):
    sub_id1 = serializers.IntegerField()
    sub_id2 = serializers.IntegerField()