
from django.contrib import admin
from django.urls import path
from .views import CustomTokenObtainPairView,LogoutAPIView,UserRegisterView
urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',CustomTokenObtainPairView.as_view()),
    path('logout/',LogoutAPIView.as_view())
]
