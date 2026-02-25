from django.contrib import admin
from .models import Sample, Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # Liste görünümünde hangi sütunlar görünsün?
    list_display = ('title', 'url_name', 'is_active', 'is_footer', 'order')
    
    # Sağ tarafta filtreleme paneli
    list_filter = ('is_active', 'is_footer')
    
    # Arama çubuğu
    search_fields = ('title', 'url_name')
    
    # Liste üzerinden doğrudan düzenlenebilir alanlar (Hızlı sıralama için)
    list_editable = ('order', 'is_active')
    
    # Varsayılan sıralama
    ordering = ('order',)

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'attachment')