from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.i18n import set_language

urlpatterns = [
    path("admin/", __import__("django.contrib.admin").contrib.admin.site.urls),
    path("i18n/setlang/", set_language, name="set_language"),
    path("", include("tours.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
