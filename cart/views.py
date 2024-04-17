from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product
from .cart import Cart
from .forms import CartAddForm


def add_to_cart(request, product_id):
    cart = Cart(request)
    if request.method == "POST":
        cart_form = CartAddForm(request.POST)
        product = get_object_or_404(Product, pk=product_id)
        if cart_form.is_valid():
            cart.add_item(
                product,
                quantity=cart_form.cleaned_data["quantity"],
                override_quantity=cart_form.cleaned_data["override_quantity"]
            )
    return redirect("cart:cart_details")


def cart_details(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddForm(initial={
            "quantity": item["quantity"],
            "override_quantity": True
        })
    return render(request, 'cart_details.html', context={"cart": cart})


def remove_from_cart(request, product_id):
    cart = Cart(request)
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        cart.remove_item(product)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
