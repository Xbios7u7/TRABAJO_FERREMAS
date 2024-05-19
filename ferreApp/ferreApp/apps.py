from django.apps import AppConfig

class FerreAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ferreApp'

    def ready(self):
        import ferreApp.signals  # Importa el archivo de señales al iniciar la aplicación
