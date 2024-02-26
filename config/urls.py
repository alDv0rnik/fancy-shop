from django.contrib import admin
from django.urls import path, include
from catalog.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'))
]


handler404 = page_not_found
