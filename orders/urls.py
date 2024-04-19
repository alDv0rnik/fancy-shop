from django.urls import path
from .views import *


app_name = "orders"

urlpatterns = [
    path("create/", create_order, name="create_order")
]

