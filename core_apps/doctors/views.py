from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Doctor
from .serializers import DoctorSerializers
from core_apps.patients.permissions import CanCreateEditPost
from core_apps.common.renderers import GenericJSONRenderer
from rest_framework import status
class CreateAndListOfDoctorAPIView(GenericAPIView):
    serializer_class = DoctorSerializers
    permission_classes = [CanCreateEditPost]
    renderer_classes=[GenericJSONRenderer]
    object_label = 'doctor'

    def get_queryset(self):
        self.object_label = 'doctors'
        return Doctor.objects.filter().order_by("-created_at")

    def get(self, request, *args, **kwargs):
        doctors = self.get_queryset()
        serializer = self.serializer_class(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            doctor=serializer.save(created_by=self.request.user)
            serializer = self.serializer_class(doctor, many=False)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSingleDoctorAndUpdateAPIView(GenericAPIView):
    serializer_class = DoctorSerializers
    permission_classes = [CanCreateEditPost]
    renderer_classes=[GenericJSONRenderer]
    lookup_field = "id"
    object_label="doctor"

    def get_queryset(self):
        return Doctor.objects.filter()

    def get_object(self):
        return super().get_object()

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        serializer = self.serializer_class(doctor)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        doctor = self.get_object()
        serializer = self.serializer_class(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        doctor = self.get_object()
        doctor.delete()
        return Response({"message": "Doctor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
