
from typing import Optional

from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework import status,generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import CreateUserSerializer
from core_apps.common.renderers import GenericJSONRenderer


User=get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=CreateUserSerializer
    renderer_classes=[GenericJSONRenderer]
    permission_classes=[AllowAny]
    object_label="user"

    def perform_create(self, serializer)->None:
        serializer.save()


def set_auth_cookies(response:Response,access_token:str,refresh_token:Optional[str]=None):
    access_token_lifetime=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()
    cookie_setting={
        "path":settings.COOKIE_PATH,
        "secure":settings.COOKIE_SECURE,
        "httponly":settings.COOKIE_HTTPONLY,
        "samesite":settings.COOKIE_SAMESITE,
        "max_age":access_token_lifetime
    }
    response.set_cookie(
        "access",access_token,**cookie_setting
    )
    if refresh_token:
        refresh_token_lifetime=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds()
        refresh_cookie_settings=cookie_setting.copy()
        refresh_cookie_settings["max_age"]=refresh_token_lifetime
        response.set_cookie(
            "refresh",refresh_token,**refresh_cookie_settings
        )
    logged_in_cookie_settings=cookie_setting.copy()
    logged_in_cookie_settings["httponly"]=False
    response.set_cookie(
        "logged_in","true",**logged_in_cookie_settings
    )


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self,request:Request,*args,**kwargs)->Response:
        token_res=super().post(request,*args,**kwargs)
        if token_res.status_code==status.HTTP_200_OK:
            access_token=token_res.data.get("access") 
            refresh_token=token_res.data.get("refresh")
            if access_token and refresh_token:
                set_auth_cookies(token_res,access_token,refresh_token)
                token_res.data["message"]="Login Successful."

            else:
                token_res.data["message"]="Login Failed"
                
        return token_res




class LogoutAPIView(APIView):
    def post(self,request:Request,*args,**kwargs):
        response=Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        response.delete_cookie("logged_in")
        return response
