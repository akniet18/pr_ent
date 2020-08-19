from rest_framework import serializers
from .models import *


class OnlineCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineCourse
        fields = "__all__"