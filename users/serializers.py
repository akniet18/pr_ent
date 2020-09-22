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
    avatar = serializers.SerializerMethodField('get_avatar_url')
    def get_avatar_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.avatar.url)
    class Meta:
        model = User
        fields = ('id', 'nickname', 'email', 'uin', 'avatar')


class ChangeUserSerializer(serializers.Serializer):
    nickname = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    uin = serializers.CharField(required=False)


class FeedbackSer(serializers.Serializer):
    text = serializers.CharField()


class AvatarSerializer(serializers.Serializer):
    avatar = serializers.CharField()