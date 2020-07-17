from django.urls import path, include
from .views import *

urlpatterns = [
    path("<id>", oneSubject.as_view()),
    path("answer/", oneAnswer.as_view())
]