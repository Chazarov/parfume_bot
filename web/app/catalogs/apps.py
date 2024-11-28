from django.apps import AppConfig
from django.core.management import call_command

class CatalogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogs'

    def ready(self) -> None:
        from catalogs.signals import session_ended, post_migrate_handler

        call_command('migrate')
        