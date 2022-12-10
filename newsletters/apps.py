from django.apps import AppConfig


class NewslettersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletters'

    def ready(self) -> None:
        import newsletters.signals