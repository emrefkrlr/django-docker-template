from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # 1. AVIF Desteğini Pillow'a Kaydet
        try:
            from pillow_heif import register_avif_opener
            register_avif_opener()
        except ImportError:
            pass

        # 2. Jeneratörleri Kaydet
        import core.image_generators