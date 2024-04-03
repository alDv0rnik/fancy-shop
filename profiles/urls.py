from django.urls import path
from profiles.views import get_profile_details, edit_profile_details


urlpatterns = [
    path("<slug:profile_slug>", get_profile_details, name='profile_details'),
    path("<slug:profile_slug>/edit", edit_profile_details, name='profile_edit'),
]