from django.conf import settings


def site_context(request):
    return {
        "LANGUAGES": settings.LANGUAGES,
        "LANGUAGE_CODE": getattr(request, "LANGUAGE_CODE", settings.LANGUAGE_CODE),
    }
