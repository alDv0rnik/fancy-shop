from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Name', max_length=50, null=False)
    image = models.ImageField(
        verbose_name="Image",
        upload_to="category/%Y/%m/%d",
        blank=True,
        default="default_cat.png"
    )
    slug = models.SlugField(max_length=50, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    def __str__(self):
        return f"{self.name}"


class ElectronicsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category__name="electronics")


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    name = models.CharField(
        verbose_name="Product name",
        max_length=200,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name="price",
        max_digits=10,
        decimal_places=2
    )
    discount = models.IntegerField(
        verbose_name="Discount",
        help_text="in percents",
        default=0
    )
    pic = models.ImageField(
        verbose_name="Picture",
        upload_to="products/%Y/%m/%d",
        blank=True,
        default="default.png"
    )
    stock = models.PositiveIntegerField(
        verbose_name="Stock",
        default=0
    )
    is_available = models.BooleanField(
        verbose_name="available",
        default=False
    )
    slug = models.SlugField(
        null=False,
        db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=['slug'])
        ]

    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})

    def __str__(self):
        return f"{self.name} - {self.price}"

    objects = models.Manager()
    electronics = ElectronicsManager()
