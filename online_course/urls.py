from django.urls import path, include
from .views import *

urlpatterns = [
    path("", OnlineCourseView.as_view())
]