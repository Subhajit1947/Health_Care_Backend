from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Patient
from .serializers import CreatePatientSerializers
from .permissions import CanCreateEditPost
from core_apps.common.renderers import GenericJSONRenderer
from rest_framework import status
class PatientAPIView(GenericAPIView):
    serializer_class = CreatePatientSerializers
    permission_classes = [CanCreateEditPost]
    renderer_classes=[GenericJSONRenderer]
    object_label = 'patient'

    def get_queryset(self):
        self.object_label = 'patients'
        return Patient.objects.filter(created_by=self.request.user).order_by("-created_at")

    def get(self, request, *args, **kwargs):
        patients = self.get_queryset()
        serializer = self.serializer_class(patients, many=True)
        return Response(serializer.data)

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient=serializer.save(created_by=self.request.user)
            serializer = self.serializer_class(patient, many=False)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSinglePatientAndUpdateAPIView(GenericAPIView):
    serializer_class = CreatePatientSerializers
    permission_classes = [CanCreateEditPost]
    renderer_classes=[GenericJSONRenderer]
    lookup_field = "id"
    object_label="patient"

    def get_queryset(self):
        return Patient.objects.filter()

    def get_object(self):
        return super().get_object()
    
    def get(self, request, *args, **kwargs):
        patient = self.get_object()
        serializer = self.serializer_class(patient)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        patient = self.get_object()
        serializer = self.serializer_class(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        patient = self.get_object()
        patient.delete()
        return Response({"message": "Patient deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
