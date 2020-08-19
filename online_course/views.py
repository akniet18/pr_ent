from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import random
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import permission_classes
from datetime import datetime


class OnlineCourseView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        queryset = OnlineCourse.objects.all()
        ser = OnlineCourseSerializer(queryset, many=True)
        return Response(ser.data)