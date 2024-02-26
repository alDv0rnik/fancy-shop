from django.urls import path
from catalog.views import *


urlpatterns = [
    path('', index),
    path("category/", categories, name='categories'),
    path("category/<int:cat>/", category, name='category'),
]