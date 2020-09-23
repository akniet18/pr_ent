from rest_framework import serializers
from .models import *


class OnlineCourseSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField('get_avatar_url')
    def get_avatar_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.avatar.url)
    class Meta:
        model = OnlineCourse
        fields = "__all__"