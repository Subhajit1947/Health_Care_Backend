
from django.urls import path,include
from .views import AssignDoctorAndRetrivePatientDoctorAPIView,GetAllDoctorAssignedToPatientAndRemoveDoctorAPIView


urlpatterns = [
    path('',AssignDoctorAndRetrivePatientDoctorAPIView.as_view()),
    path('<uuid:id>/',GetAllDoctorAssignedToPatientAndRemoveDoctorAPIView.as_view()),   
]
