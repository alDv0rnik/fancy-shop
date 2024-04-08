from django.urls import path
from catalog.views import *


urlpatterns = [
    # path("", ShopHome.as_view(), name='categories'),
    path("<slug:category_slug>/", category, name='category'),
]