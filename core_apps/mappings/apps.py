from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MappingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.mappings'
    verbose_name=_("Mappings")
