
from django.urls import path,include
from .views import CreateAndListOfDoctorAPIView,GetSingleDoctorAndUpdateAPIView


urlpatterns = [
    path('',CreateAndListOfDoctorAPIView.as_view()),
    path('<uuid:id>/',GetSingleDoctorAndUpdateAPIView.as_view()),   
]
