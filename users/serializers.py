from rest_framework import serializers
from .models import *


class PhoneS(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=50)

class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField()


class historySerializerCreate(serializers.Serializer):
    subject1 = serializers.CharField()
    subject2 = serializers.CharField(required=False)
    right_answers = serializers.CharField()

class historySerializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = "__all__"
        read_only_fields = ("type_test", "count_of_questions", "user")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'email', 'uin')


class FeedbackSer(serializers.Serializer):
    text = serializers.CharField()