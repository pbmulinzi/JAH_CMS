from django.apps import AppConfig


class Jah_AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Jah_Accounts'

    def ready(self):
        import Jah_Accounts.signals
