from rest_framework import serializers
from .models import *


class PhoneS(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=50)

class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField()


class historySerializerCreate(serializers.Serializer):
    subject = serializers.CharField()
    right_answers = serializers.CharField()

class historySerializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'email', 'uin')