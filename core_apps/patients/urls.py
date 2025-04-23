
from django.urls import path,include
from .views import PatientAPIView,GetSinglePatientAndUpdateAPIView


urlpatterns = [

    path('',PatientAPIView.as_view()),
    path('<uuid:id>/',GetSinglePatientAndUpdateAPIView.as_view()),
    
]
