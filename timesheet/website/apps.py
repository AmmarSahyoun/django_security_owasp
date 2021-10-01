from django.apps import AppConfig

class WebsiteAppConfig(AppConfig):
    name = 'website'

    def ready(self):
        import website.signals
