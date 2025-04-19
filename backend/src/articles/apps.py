from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    """
    Configuration for the Articles application.
    """
    name = 'articles'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Articles Management'

    def ready(self):
        """
        Import signals when the app is ready.
        """
        # Import signals to register them
        # This is commented out as we don't have signals yet, but it's a good practice
        # import articles.signals
