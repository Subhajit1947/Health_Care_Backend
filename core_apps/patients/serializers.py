from rest_framework import serializers
from .models import Patient

class CreatePatientSerializers(serializers.ModelSerializer):
    creator_username=serializers.ReadOnlyField(source="created_by.username")
    class Meta:
        model=Patient
        fields=['id','name','age','gender','creator_username','address','phone']
        read_only_fields=['pkid','id','creator_username']
    



