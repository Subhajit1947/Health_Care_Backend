from rest_framework import serializers
from .models import Doctor

class DoctorSerializers(serializers.ModelSerializer):
    creator_username=serializers.ReadOnlyField(source="created_by.username")
    class Meta:
        model=Doctor
        fields=['id','name','age','specialization','gender','creator_username','phone','created_at']
        read_only_fields=['pkid','id','creator_username','created_at']