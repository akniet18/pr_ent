from django.urls import path, include
from .views import *

urlpatterns = [
    path("<id>", OnlineCourseView.as_view())
]