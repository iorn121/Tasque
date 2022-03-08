from django.apps import AppConfig
from django.db.models.signals import post_migrate


class TasqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasque'

    # migrate時に関数実行
    def ready(self):
        from .models import create_default_tag
        post_migrate.connect(create_default_tag, sender=self)
