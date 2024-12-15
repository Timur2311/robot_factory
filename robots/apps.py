from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'

    def ready(self) -> None:
        import robots.signals  # noqa