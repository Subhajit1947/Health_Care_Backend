from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimeStampedModel
from django.contrib.auth import get_user_model

User=get_user_model()

class Doctor(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE=("male",_("Male"))
        FEMALE=("female",_("female"))
        OTHER=("other",_("Other"))
    
    class Specialization(models.TextChoices):
        CARDIOLOGIST = "cardiologist", _("Cardiologist")
        DERMATOLOGIST = "dermatologist", _("Dermatologist")
        NEUROLOGIST = "neurologist", _("Neurologist")
        PEDIATRICIAN = "pediatrician", _("Pediatrician")
        PSYCHIATRIST = "psychiatrist", _("Psychiatrist")
        ORTHOPEDIC = "orthopedic", _("Orthopedic")
        ENT = "ent", _("ENT (Ear, Nose, Throat)")
        GYNECOLOGIST = "gynecologist", _("Gynecologist")
        ONCOLOGIST = "oncologist", _("Oncologist")
        GENERAL = "general", _("General Physician")

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender=models.CharField(
        verbose_name=_("Gender"),
        max_length=10,
        choices=Gender.choices,
        default=Gender.OTHER
    )
    specialization=models.CharField(
        verbose_name=_("Specialization"),
        max_length=30,
        choices=Specialization.choices,
        default=Specialization.GENERAL
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_by=models.ForeignKey(
        User,verbose_name=_("Creator"),on_delete=models.CASCADE,
        related_name="doctors"
    )
    class Meta:
        verbose_name=_("Doctor")
        verbose_name_plural=_("Doctors")
