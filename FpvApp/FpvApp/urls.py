"""import block"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fpv_app_admin/', admin.site.urls),
    path('', include("FpvAppMain.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
