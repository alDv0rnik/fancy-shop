from django.db import models

from catalog.models import Product
from profiles.models import Profile
from enum import Enum


ORDER_STATUS_CHOICES = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
)


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name='Status',
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order - {self.pk}"

    @property
    def total_cost(self):
        return sum(item.get_cost for item in self.items.all())

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        indexes = [
            models.Index(fields=["-created_at"])
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    price = models.DecimalField(
        verbose_name="price",
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=1)

    def __str__(self):
        return f"{self.pk}"

    def get_cost(self):
        return self.price * self.quantity

