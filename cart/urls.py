from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path("", cart_details, name="cart_details"),
    path("add/<int:product_id>", add_to_cart, name="cart_add"),
    path("remove/<int:product_id>", remove_from_cart, name="cart_remove")
]
