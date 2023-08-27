from django.contrib import admin
from django.urls import path, re_path, include
from aplications.employees import views
from django.conf import settings
from django.conf.urls.static import static
# Con esta variable se da un nombre a el conjunto de urls
app_name = "externas_app"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('aplications.employees.url')),
    path('', include('aplications.departments.url')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
