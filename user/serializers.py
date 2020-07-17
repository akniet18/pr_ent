from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class registerSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(min_length=8)


class loginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(min_length=8)