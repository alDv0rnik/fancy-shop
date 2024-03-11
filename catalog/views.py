from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Category, Product

cats = {
    "food": "food",
    "animal-goods": "animal goods"
}

menu = ["Home", "About", "Contacts", "FAQ"]


def index(request):
    categories = Category.objects.all()
    return render(
        request,
        "index.html",
        context={
            "title": "My Shop - Main page",
            "menu": menu,
            "categories": categories
        }
    )


def about(request):
    return render(request, "about.html")


def categories(request):
    return HttpResponse("<h3>Catalog</h3>")


def category(request, category_slug):
    products = Product.objects.all()
    if category_slug == "electronics":
        products = Product.electronics.all()

    context = {
        "products": products
    }
    return render(request, "products.html", context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")
