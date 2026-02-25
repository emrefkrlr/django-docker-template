from django.db import models
from .image_service import apply_watermark
from django.utils.translation import gettext_lazy as _ # <-- Ekleyin

class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Başlık"))    
    url_name = models.CharField(max_length=255, blank=True, null=True)
    url_external = models.URLField(blank=True, null=True, help_text="Dış bağlantı varsa burayı doldurun.")
    is_active = models.BooleanField(default=True)
    is_footer = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Menü"
        verbose_name_plural = "Menüler"

    def __str__(self):
        return self.title

class Sample(models.Model):
    attachment = models.ImageField(upload_to='samples/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.attachment and hasattr(self.attachment, 'path'):
            apply_watermark(self.attachment.path)