from django.urls import path, include
from .views import *

urlpatterns = [
    path("oneSubject/<id>", pass_oneSubject.as_view()),
    path('pass', pass_ENT.as_view()),

    path('answers/<id>', Answers.as_view()),
    path("question", Extension.as_view())
]