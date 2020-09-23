from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.db.models import Count
import random
from django.http import JsonResponse
import json
from utils.compress import *

def get_random_question(subject, default=False):
    if default:
        questions = list(subject.test_subject.all())
        random.shuffle(questions)
        questions = questions[:20]
        return questions
    else:
        questions1 = list(subject.test_subject.annotate(number_of_answers=Count('question_variant')).filter(number_of_answers = 5))
        random.shuffle(questions1)
        questions1 = questions1[:20]
        questions2 = list(subject.test_subject.annotate(number_of_answers=Count('question_variant')).filter(number_of_answers = 8))
        random.shuffle(questions2)
        questions2 = questions2[:10]
        questions = questions1 + questions2
        return questions


class pass_oneSubject(APIView):
    permission_classes = [permissions.AllowAny,]

    def get(self, request, id):
        subject = Subject.objects.get(id = id)
        questions = None
        if id=='1' or id == '2' or id == '3':
            questions = get_random_question(subject, True)
        else:
            questions = get_random_question(subject)
        s = TestSer(questions, many=True, context={'request': request})
        return Response(s.data)


class pass_ENT(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        s = passEntSer(data = request.data)
        if s.is_valid():
            # default subjects
            def_sbj1 = Subject.objects.get(id = 1)
            def_sbj2 = Subject.objects.get(id = 2)
            def_sbj3 = Subject.objects.get(id = 3)
            math_log = get_random_question(def_sbj1, True)
            math_log = TestSer(math_log, many=True, context={'request': request})
            history = get_random_question(def_sbj2, True)
            history = TestSer(history, many=True, context={'request': request})
            literacy = get_random_question(def_sbj3, True)
            literacy = TestSer(literacy, many=True, context={'request': request})
            # choosen subjects
            # 1
            sub_id1 = s.validated_data['sub_id1']
            subject = Subject.objects.get(id = sub_id1)
            first_sbj = get_random_question(subject)
            first_sbj = TestSer(first_sbj, many=True, context={'request': request})
            # 2
            sub_id2 = s.validated_data['sub_id2']
            subject = Subject.objects.get(id = sub_id2)
            second_sbj = get_random_question(subject)
            second_sbj = TestSer(second_sbj, many=True, context={'request': request})
            data = {
                'math_log': math_log.data,
                'history': history.data,
                "literacy": literacy.data,
                'sub1': first_sbj.data,
                'sub2': second_sbj.data
            }
            return Response(data)
        else:
            return Response(s.errors)
            


class Answers(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        subject = Subject.objects.get(id = id)
        questions = subject.test_subject.all()
        s = TestSer2(questions, many=True,context={'request': request})
        return Response(s.data)



class Extension(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        s = ExtensionSer(data=request.data)
        if s.is_valid():
            question = s.validated_data['question']
            images = s.validated_data['images']
            for i in images:
                im = base64img(i, request.user.id)
                img = compress_image(im, (200, 200))
                
            return Response({"status": "ok"})
        else:
            return Response(s.errors)