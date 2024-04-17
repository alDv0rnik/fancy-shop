from django.urls import path
from catalog.views import *


app_name = 'catalog'


urlpatterns = [
    path("<slug:category_slug>/", category, name='category'),
    path(
        "<slug:category_slug>/<slug:product_slug>",
        ProductDetail.as_view(),
        name='product_detail'
    )
]