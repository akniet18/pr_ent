from django.shortcuts import render
from .serializers import *

from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Register(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        s = registerSerializer(data=request.data)
        if s.is_valid():
            phone = s.validated_data['phone']
            pwd = s.validated_data['password']
            if User.objects.filter(username=phone).exists():
                return Response({"status": "user is already exists"})
            else:
                u = User.objects.create(
                    username = phone,
                    password = pwd
                )
                return Response({"status": "created"})
        else:
            return Response(s.errors)

    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        s = loginSerializer(data=request.data)
        if s.is_valid():
            phone = s.validated_data['phone']
            pwd = s.validated_data['password']
            user = User.objects.filter(username = phone)
            if user.exists():
                if user[0].check_password(pwd):
                    token, created = Token.objects.get_or_create(user=user[0])
                    return Response({"status": "created", "token": token.key})
                else:
                    return Response({'status': "the username or password is incorrect"})
            else:
                return Response({"status": "the username or password is incorrect"})
        else:
            return Response(s.errors)