from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class oneSubject(APIView):
    permission_classes = [permissions.AllowAny,]

    def get(self, request, id):
        subject = Subject.objects.get(id = id)
        tests = subject.test_subject.all()
        s = TestSer(tests, many=True)
        return Response(s.data)


class oneAnswer(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        s = AnswerOneSer(data=request.data)
        if s.is_valid():
            variant = Variant.objects.get(id=s.validated_data['answer_id'], test_id = s.validated_data['test_id'])
            return Response({'status': variant.is_right})
        else: 
            return Response(s.errors)