from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import random
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from django.contrib.auth import (login as django_login,
                                 logout as django_logout)
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView, RetrieveUpdateAPIView
from datetime import datetime
from entapp.models import *
from utils.compress import *
from django.core.mail import send_mail
from django.conf import settings

# from django_auto_prefetching import AutoPrefetchViewSetMixin


class PhoneCode(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        s = PhoneS(data=request.data)
        rand = random.randint(1000, 9999)
        if s.is_valid():
            nickname = s.validated_data['name']
            phone = s.validated_data['phone']
            if phone[0] != "+":
                phone = "+" + phone
            print('code generate: ',s.validated_data, rand)
            if PhoneOTP.objects.filter(phone = phone).exists():
                a = PhoneOTP.objects.get(phone = phone)
                a.nickname = nickname
                a.otp = rand
                # a.otp = "1111"
                a.save()
            else:
                PhoneOTP.objects.create(phone=phone, otp=str(rand), nickname=nickname)
                # PhoneOTP.objects.create(phone=phone, nickname=nickname, otp=str(1111))
            # smsc.send_sms(s.validated_data['phone'], "Код подтверждения: "+str(rand) + " Fixup", sender="sms")
            return Response({'status': 'ok'})
        else:
            return Response(s.errors)


class Register(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        s = RegisterSerializer(data=request.data)
        if s.is_valid():
            print('register: ', s.validated_data['phone'], s.validated_data['code'])
            phone = s.validated_data['phone']
            if phone[0] != "+":
                phone = "+" + phone
            u = PhoneOTP.objects.get(phone=phone)
            if u.otp == str(s.validated_data['code']):
                # u.validated = True
                nickname = u.nickname
                # u.save()
                if User.objects.filter(phone=phone).exists():
                    us = User.objects.get(phone=phone)
                    uid = us.pk
                    us.nickname = nickname
                    us.save()
                else:
                    us = User.objects.create(phone=phone)
                    uid = us.pk
                if Token.objects.filter(user=us).exists():
                    token = Token.objects.get(user=us)
                else:
                    token = Token.objects.create(user=us)
                # user = authenticate(phone=phone)
                # django_login(request, us)
                return Response({'key': token.key, 'uid': uid, 'status': 'ok'})
            else:
                return Response({'status': 'otp error'})
        else:
            return Response(s.errors)


class historyView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        queryset = history.objects.filter(user = request.user)
        s = historySerializer(queryset, many=True)
        return Response(s.data)

    def post(self, request):
        s = historySerializer(data=request.data)
        if s.is_valid():
            right_answers = s.validated_data['right_answers']
            subject1 = s.validated_data['subject1']
            subject2 = s.validated_data.get('subject2', None)
            count_of_question = 0
            subject_name = ""
            if subject2:
                history.objects.create(
                    user = request.user,
                    right_answers = right_answers,
                    count_of_questions = 140,
                    type_test = "ent",
                    subject1 = Subject.objects.get(id = subject1).name,
                    subject2 = Subject.objects.get(id = subject2).name
                )
            elif (subject1 == '1' or subject1 == '2' or subject1 == '3') and subject2 == None:
                history.objects.create(
                    user = request.user,
                    right_answers = right_answers,
                    count_of_questions = 20,
                    type_test = "OneSubject",
                    subject1 = Subject.objects.get(id = subject1).name,
                    # subject2 = Subject.objects.get(id = subject2).name
                )
            else:
                history.objects.create(
                    user = request.user,
                    right_answers = right_answers,
                    count_of_questions = 40,
                    type_test = "OneSubject",
                    subject1 = Subject.objects.get(id = subject1).name,
                    # subject2 = Subject.objects.get(id = subject2).name
                )
            return Response({'status': "ok"})
        else:
            return Response(s.errors)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, id):
        queryset = User.objects.get(id=id)
        s = UserSerializer(queryset, context={'request': request})
        return Response(s.data)

    def post(self, request, id):
        s = ChangeUserSerializer(data=request.data)
        if s.is_valid():
            user = User.objects.get(id=id)
            # user.first_name = s.validated_data.get('first_name', user.first_name)
            user.nickname = s.validated_data.get('nickname', user.nickname)
            user.uin = s.validated_data.get('uin', user.uin)
            email = s.validated_data.get('email', None)
            if email != user.email and email:
                user.email = email
            user.save()
            s = UserSerializer(user, context={'request': request})
            return Response(s.data)
        else:
            return Response(s.errors)


class Avatar(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        s = AvatarSerializer(data=request.data)
        if s.is_valid():
            ava = s.validated_data['avatar']
            img = base64img(ava, 'avatar')
            avatar = compress_image(img, (200, 200))
            request.user.avatar = avatar
            request.user.save()
            return Response({'status': "ok", "avatar": request.user.avatar.url})
        else:
            return Response(s.errors)


# import ssl, smtplib

class FeedBackView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        s = FeedbackSer(data=request.data)
        if s.is_valid():
            message = s.validated_data['text']
            message += "\n\n" + "phone: " + request.user.phone
            if request.user.email:
                message += "\nemail: " + request.user.email
            receiver_email = "akniet1805@gmail.com"
            send_mail(
                'Subject here',
                message,
                settings.EMAIL_HOST_USER,
                [receiver_email, ],
                fail_silently=False,
            )
            return Response({'status': 'ok'})
            
            # port = 465  # For starttls
            # smtp_server = "smtp.gmail.com"
            # sender_email = "bilimcenter20@gmail.com"
            # password = "Bilim20centre20"
            # message = s.validated_data['text']
            # if request.user.is_authenticated:
            #     message += "\n\n" + "phone: " + request.user.phone + "\nemail: " + request.user.email
            
            # context = ssl.create_default_context()
            # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            #     server.login(sender_email, password)
            #     server.sendmail(sender_email, receiver_email, message)
        else:
            return Response(s.errors)

