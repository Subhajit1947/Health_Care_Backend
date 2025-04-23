
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include("core_apps.users.urls")),
    path('api/patients/',include("core_apps.patients.urls")),
    path('api/doctors/',include("core_apps.doctors.urls")),
    path('api/mappings/',include("core_apps.mappings.urls")),
]
admin.site.site_header="Health Care Admin"
admin.site.site_title="Health Care Admin Portal"
admin.site.index_title="Wellcome to Health Care Admin Portal"
