from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', Register.as_view()),
    path('login', LoginView.as_view()),
]