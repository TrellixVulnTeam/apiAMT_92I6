from django.apps import AppConfig


class CsvsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CSVS'

    def ready(self):
    	import CSVS.signals # register the signals
