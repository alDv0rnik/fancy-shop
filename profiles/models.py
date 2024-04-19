from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

from catalog.models import Product


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile_user"
    )
    phone_number = models.CharField(
        verbose_name="Phone",
        max_length=50,
        blank=True
    )
    shipping_address = models.CharField(
        verbose_name="Address",
        max_length=100,
        blank=True
    )
    postcode = models.CharField(
        verbose_name="Postcode",
        max_length=50,
        blank=True
    )
    city = models.CharField(
        verbose_name="City",
        max_length=100,
        blank=True
    )
    nickname = models.CharField("Nickname", max_length=100, default="")
    avatar = models.ImageField("Avatar", upload_to="users/", default="default_user.jpg")
    slug = AutoSlugField(max_length=100, populate_from=('nickname',))
    favourites = models.ManyToManyField(
        Product,
        blank=True,
        default=None,
        related_name="fav_product"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_slug": self.slug})

    def __str__(self):
        return f"{self.pk} - {self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

