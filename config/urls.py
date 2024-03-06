from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from catalog.views import page_not_found, index, about


urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = page_not_found
