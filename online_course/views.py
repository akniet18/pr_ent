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

    def get(self, request, id):
        queryset = OnlineCourse.objects.filter(type_cours = id)
        ser = OnlineCourseSerializer(queryset, many=True, context={'request': request})
        return Response(ser.data)