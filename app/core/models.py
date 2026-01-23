from django.db import models
from .image_service import apply_watermark

class Sample(models.Model):
    # Resim işlemleri yapacağımız için ImageField daha uygun
    attachment = models.ImageField(upload_to='samples/')

    def save(self, *args, **kwargs):
        # 1. Önce dosyayı kaydet
        super().save(*args, **kwargs)
        
        # 2. Eğer dosya varsa ve bir resimse watermark uygula
        if self.attachment and hasattr(self.attachment, 'path'):
            apply_watermark(self.attachment.path)