from django.conf import settings


def site_settings(request):
    """
    Context processor to add site-wide settings to all templates
    """
    return {
        'SITE_NAME': 'Blog & Education Platform',
        'SITE_DESCRIPTION': 'Learn and grow with our educational content',
        'DEBUG': settings.DEBUG,
    }
