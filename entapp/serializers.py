from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class SubjectSer(serializers.ModelSerializer):
    class Meta:
        model = Subject()
        fields = "__all__"

class PhotoSer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_avatar_url')
    def get_avatar_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.photo.url)
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

class TestSer2(serializers.ModelSerializer):
    rights = VariantSer(many=True)
    question_photo = PhotoSer(many=True)
    class Meta:
        model = Question()
        fields = ('text', 'rights', 'question_photo')


class AnswerOneSer(serializers.Serializer):
    test_id = serializers.CharField()
    answer_id = serializers.CharField()


class passEntSer(serializers.Serializer):
    sub_id1 = serializers.IntegerField()
    sub_id2 = serializers.IntegerField()


class ExtensionSer(serializers.Serializer):
    images = serializers.ListField(child=serializers.CharField(), required=False)
    question = serializers.CharField()