from django.urls import path, include
from .views import *

urlpatterns = [
    path('phone/otp/', PhoneCode.as_view()),
    path('register/', Register.as_view()),
    path("history", historyView.as_view()),
    path('<id>/', UserView.as_view()),
    path('avatar', Avatar.as_view()),
    
    path('feedback', FeedBackView.as_view())
]