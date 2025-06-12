from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

    def ready(self):
        """
        Metodo que se ejecuta cuando la app está lista 
        E importar aqui los signals evita problemas de importacion
        circular.
        """
        from product import signals
        return super().ready()