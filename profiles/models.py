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
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=200)
    email = models.EmailField("email", max_length=200)
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

