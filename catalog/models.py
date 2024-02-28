from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=50, null=False)
    slug = models.SlugField(max_length=50, null=False)

    class Meta:
        verbose_name  = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.name} - {self.price}"
