from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from catalog.views import page_not_found, ShopHome, about, search
from profiles.views import register_user, login_user, logout_user


urlpatterns = [
    path('', ShopHome.as_view(), name="home"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('profile/', include('profiles.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('search/', search, name="search_result"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = page_not_found
