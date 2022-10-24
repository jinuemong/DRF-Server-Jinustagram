from django.apps import AppConfig


class PostingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posting'

    def ready(self):
        from .jobs import updater
        updater.start()    