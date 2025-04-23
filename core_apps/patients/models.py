from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimeStampedModel
from django.contrib.auth import get_user_model

User=get_user_model()

class Patient(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE=("male",_("Male"))
        FEMALE=("female",_("female"))
        OTHER=("other",_("Other"))

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender=models.CharField(
        verbose_name=_("Gender"),
        max_length=10,
        choices=Gender.choices,
        default=Gender.OTHER
    )
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_by=models.ForeignKey(
        User,verbose_name=_("Creator"),on_delete=models.CASCADE,
        related_name="patients"
    )

    class Meta:
        verbose_name=_("Patient")
        verbose_name_plural=_("Patients")
