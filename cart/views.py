from typing import Iterable

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from cart.cart import Cart
from catalog.models import Product
from .forms import CartAddForm


def add_to_cart(request, product_id):
    cart = Cart(request)
    if request.method == "POST":
        cart_form = CartAddForm(request.POST)
        product = get_object_or_404(Product, pk=product_id)
        if cart_form.is_valid():
            cart.add_item(
                product=product,
                quantity=cart_form.cleaned_data["quantity"],
                override_quantity=cart_form.cleaned_data["override_quantity"]
            )
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        cart.remove_item(product)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddForm(initial={
            'quantity': item['quantity'],
            'override_quantity': True})
    return render(request, 'details.html', {'cart': cart})