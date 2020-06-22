from django.apps import AppConfig


class QuestionapiConfig(AppConfig):
    name = 'questionapi'

    def ready(self):
        import questionapi.signals
