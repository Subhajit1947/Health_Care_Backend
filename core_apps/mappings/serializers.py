from rest_framework import serializers
from .models import PatientDoctorMapping
from core_apps.doctors.models import Doctor
from core_apps.patients.models import Patient

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    
    patient_name=serializers.ReadOnlyField(source="patient.name")
    doctor_name=serializers.ReadOnlyField(source="doctor.name")
    name_of_assigned_by=serializers.ReadOnlyField(source="assigned_by.get_full_name")

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient_name','doctor_name','name_of_assigned_by','notes','created_at']
        read_only_fields=['id','patient_name','doctor_name','name_of_assigned_by','created_at']
    