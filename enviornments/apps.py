from django.apps import AppConfig


class EnviornmentsConfig(AppConfig):
    name = 'enviornments'

	
    def ready(self):
		import enviornments.signals