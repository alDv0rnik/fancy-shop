from django.urls import path
from profiles.views import (
    get_profile_details,
    edit_profile_details,
    get_favourites_list,
    add_to_favourites
)


urlpatterns = [
    path("<slug:profile_slug>", get_profile_details, name='profile_details'),
    path("<slug:profile_slug>/edit", edit_profile_details, name='profile_edit'),
    path("<slug:profile_slug>/fav", get_favourites_list, name='favourites_list'),
    path("<slug:profile_slug>/fav/<int:product_id>", add_to_favourites, name='add_favourites'),
]