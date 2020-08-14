from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()


class PhoneS(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=50)

class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField()