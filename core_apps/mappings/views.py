from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from core_apps.patients.permissions import CanCreateEditPost
from core_apps.common.renderers import GenericJSONRenderer
from core_apps.doctors.serializers import DoctorSerializers
from core_apps.patients.models import Patient
from core_apps.doctors.models import Doctor
class AssignDoctorAndRetrivePatientDoctorAPIView(GenericAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [CanCreateEditPost]
    renderer_classes=[GenericJSONRenderer]
    object_label = 'patient_doctor_mapping'

    def get_queryset(self):
        self.object_label = 'patient_doctor_mappings'
        return PatientDoctorMapping.objects.all().order_by("-created_at")

    def get(self, request, *args, **kwargs):
        patient_doctors = self.get_queryset()
        serializer = self.serializer_class(patient_doctors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        patient_id=request.data.get('patient')
        doctor_id=request.data.get('doctor')
        notes=request.data.get('notes')
        if patient_id and doctor_id:
            try:
                patient=Patient.objects.get(id=patient_id)
                doctor=Doctor.objects.get(id=doctor_id)
            except:
                return Response({"message": "Somthing went wrong"}, status=400)
        serializer = self.get_serializer(data={'notes':notes})
        serializer.is_valid(raise_exception=True)
        serializer.save(assigned_by=request.user,patient=patient,doctor=doctor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class GetAllDoctorAssignedToPatientAndRemoveDoctorAPIView(GenericAPIView):
    serializer_class = DoctorSerializers
    permission_classes = [CanCreateEditPost]
    renderer_classes=[GenericJSONRenderer]
    object_label="doctor_assigned"

    def get(self, request, *args, **kwargs):
        patient_id = kwargs.get('id') 
        patient=Patient.objects.get(id=patient_id)
        mappings = PatientDoctorMapping.objects.filter(patient=patient).order_by("-created_at")
        doctors=[row.doctor for row in mappings ]
        serializer = self.serializer_class(doctors,many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        doctor_to_remove =PatientDoctorMapping.objects.get(id=id)
        doctor_to_remove.delete()
        return Response({"message": "Doctor remove successfully"}, status=204)

