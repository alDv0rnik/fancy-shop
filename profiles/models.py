from django.db import models


class Profile(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=200)
    email = models.EmailField("email", max_length=200)
    nickname = models.CharField("Nickname", max_length=100, default="")

