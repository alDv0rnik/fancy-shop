from django.urls import path
from catalog.views import *


urlpatterns = [
    path('', index),
    path("category/", categories, name='categories'),
    path("category/<slug:category_slug>/", category, name='category'),
]