from django.conf import settings
from .models import Menu

def global_context(request):
    try:
        main_menu_qs = Menu.objects.filter(is_active=True, is_footer=False)
        main_menu = list(main_menu_qs) if main_menu_qs.exists() else [
            {'title': 'Anasayfa', 'url_name': 'core:index'},
            {'title': 'Yönetim Paneli', 'url_name': 'admin:index'},
        ]
        
        footer_menu_qs = Menu.objects.filter(is_active=True, is_footer=True)
        footer_menu = list(footer_menu_qs) if footer_menu_qs.exists() else [
            {'title': 'GitHub', 'url_external': 'https://github.com/emrefkrlr/django-docker-template'},
        ]
    except Exception:
        main_menu = [{'title': 'Anasayfa', 'url_name': 'core:index'}]
        footer_menu = []

    return {
        'project_name': getattr(settings, 'PROJECT_NAME', 'Django Project Template'),
        'project_version': getattr(settings, 'PROJECT_VERSION', '1.0.0'),
        'main_menu': main_menu,
        'footer_menu': footer_menu,
        'contact_info': getattr(settings, 'CONTACT_INFO', {}),
        'social_links': getattr(settings, 'SOCIAL_LINKS', {}),
        'system_notifications': {
            'maintenance_mode': getattr(settings, 'MAINTENANCE_MODE', False),
            'announcement': getattr(settings, 'SITE_ANNOUNCEMENT', None),
        },
        'is_debug': settings.DEBUG,
    }