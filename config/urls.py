from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from catalog.views import page_not_found, index, about
from profiles.views import register_user, login_user, logout_user


urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = page_not_found
