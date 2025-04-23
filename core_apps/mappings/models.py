from core_apps.common.models import TimeStampedModel
from django.db import models
from core_apps.doctors.models import Doctor
from core_apps.patients.models import Patient
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User=get_user_model()

class PatientDoctorMapping(TimeStampedModel):
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings")
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    class Meta:
        unique_together = ('patient', 'doctor')
        verbose_name=_("Patient-Doctor Mapping")
        verbose_name_plural=_("Patient-Doctor Mappings")

