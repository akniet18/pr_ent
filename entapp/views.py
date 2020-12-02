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
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.conf import settings


def get_random_question(subject, default=False):
    if default:
        if subject.id == 2:
            questions = list(subject.test_subject.all())
            random.shuffle(questions)
            l = len(questions)
            l = l // 20
            r = random.randint(0, l-1)
            questions = questions[r*20:(r+1)*20]
            return questions
        else:
            questions = list(subject.test_subject.all().distinct('text'))
            random.shuffle(questions)
            questions = questions[:20]
            return questions
    else:
        q = subject.test_subject.all().distinct('text')
        questions1 = list(subject.test_subject.annotate(
            number_of_answers=Count('question_variant')).filter(number_of_answers = 5, id__in=q)
        )
        random.shuffle(questions1)
        questions1 = questions1[:20]
        questions2 = list(subject.test_subject.annotate(
            number_of_answers=Count('question_variant')).filter(number_of_answers = 8, id__in=q)
        )
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
        return Response({'data': s.data, "subject": subject.name})


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
            subject1 = Subject.objects.get(id = sub_id1)
            first_sbj = get_random_question(subject1)
            first_sbj = TestSer(first_sbj, many=True, context={'request': request})
            # 2
            sub_id2 = s.validated_data['sub_id2']
            subject2 = Subject.objects.get(id = sub_id2)
            second_sbj = get_random_question(subject2)
            second_sbj = TestSer(second_sbj, many=True, context={'request': request})
            data = {
                'math_log': math_log.data,
                'history': history.data,
                "literacy": literacy.data,
                'sub1': {'data':first_sbj.data, "subject": subject1.name},
                'sub2': {'data':second_sbj.data, "subject": subject2.name}
            }
            return Response(data)
        else:
            return Response(s.errors)
            


class Answers(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        subject = Subject.objects.get(id = id)
        questions = list(subject.test_subject.all())
        random.shuffle(questions)
        questions = questions[:30]
        s = TestSer2(questions, many=True,context={'request': request})
        return Response(s.data)



def logo_data(logo_data):
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo
class Extension(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        s = ExtensionSer(data=request.data)
        if s.is_valid():
            # if request.user.is_paid:
                question = s.validated_data['question']
                images = s.validated_data.get('images', None)
                
                m = EmailMultiAlternatives(
                    subject="subject",
                    body=question,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER,]
                )
                if images:
                    for i in images:
                        im = base64img(i, str(request.user.id)+request.user.phone)
                        img = compress_image(im, (200, 200))
                        m.attach(logo_data(img.read()))

                m.send(fail_silently=False)
                return Response({"status": "ok"})
            # else:
                # return Response({'status': 'not paid'})
        else:
            return Response(s.errors)


from io import BytesIO
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class loadtest(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        s = loadtetsSer(data=request.data)
        if s.is_valid():
            dataf = s.validated_data['dataf']
            with open(os.path.join(BASE_DIR, 'entapp/fixtures/'+dataf), encoding='utf-8') as json_file:
                data = json.load(json_file)
                sub = Subject.objects.get(id=3)
                for i in data:
                    q = Question.objects.create(text = i['q'], subject = sub)
                    if i['r'] == i['a']:
                        question_variant.objects.create(text=i['a'], question = q, is_right=True)
                    else:
                        question_variant.objects.create(text=i['a'], question = q)

                    if i['r'] == i['b']:
                        question_variant.objects.create(text=i['b'], question = q, is_right=True)
                    else:
                        question_variant.objects.create(text=i['b'], question = q)

                    if i['r'] == i['c']:
                        question_variant.objects.create(text=i['c'], question = q, is_right=True)
                    else:
                        question_variant.objects.create(text=i['c'], question = q)

                    if i['r'] == i['d']:
                        question_variant.objects.create(text=i['d'], question = q, is_right=True)
                    else:
                        question_variant.objects.create(text=i['d'], question = q)
                    
                    if i['r'] == i['e']:
                        question_variant.objects.create(text=i['e'], question = q, is_right=True)
                    else:
                        question_variant.objects.create(text=i['e'], question = q)
                        # if 'f' in i:
                        #     question_variant.objects.create(text=i['F'], question = q)
                        #     question_variant.objects.create(text=i['G'], question = q)
                        #     question_variant.objects.create(text=i['H'], question = q)
            return Response({'status': 'ok'})
        else:
            return Response(s.errors)