from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "stock", "created_at")
    readonly_fields = [
        "created_at",
        "get_image"
    ]
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.pic.url} width="110" height="100">')

    get_image.short_description = "Image"
