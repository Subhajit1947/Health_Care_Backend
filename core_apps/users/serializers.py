from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
User=get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","first_name","last_name"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



    
class CustomUserSerializer(serializers.ModelSerializer):
    full_name=serializers.ReadOnlyField(source="get_full_name")
    # gender=serializers.ReadOnlyField(source="profile.gender")
    # occupation=serializers.ReadOnlyField(source="profile.occupation")

    class Meta:
        model=User
        fields=[
            "id","email","first_name","last_name","username",
            "full_name","gender","occupation","date_joined"
        ]
        read_only_fields=["id","email","date_joined"]






