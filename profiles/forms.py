from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from profiles.models import Profile
from .utils import update_profile


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First name",
                "class": "form-control rounded-4",
                "style": "max-width: 200px; margin-left: auto; margin-right: auto;"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Last name",
                "class": "form-control rounded-4",
                "style": "max-width: 200px; margin-left: auto; margin-right: auto;"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "form-control rounded-4",
                "style": "max-width: 200px; margin-left: auto; margin-right: auto;"
            })
        }

    def save(self, *args, **kwargs):
        instance = super(UserEditForm, self).save(*args, **kwargs)
        update_profile(instance)
        return instance


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["avatar"]


class ShippingOrderEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["phone_number", "shipping_address", "postcode", "city"]
