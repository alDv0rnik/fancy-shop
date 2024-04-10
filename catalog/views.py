import logging

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Product


logger = logging.getLogger('fancy-shop-logger')


class ShopHome(ListView):
    model = Category
    template_name = "index.html"
    context_object_name = "categories"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShopHome, self).get_context_data(**kwargs)
        context["title"] = "My Shop - Main page"
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["title"] = f"My Shop - {self.model.name}"
        return context


def about(request):
    return render(request, "about.html")


def category(request, category_slug):
    products = Category.objects.get(slug=category_slug).products.all()
    logger.info(f"Get all products for category {category_slug}")
    context = {
        "products": products
    }
    return render(request, "products.html", context=context)


def search(request):
    query = request.GET.get("q")
    products = Product.objects.filter(name__icontains=query)
    context = {
        "products": products
    }
    return render(request, "products.html", context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")
