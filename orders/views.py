from django.shortcuts import render

from cart.cart import Cart
from orders.models import Order, OrderItem
from profiles.forms import ShippingInfoEditForm


def create_order(request):
    cart = Cart(request)
    profile = request.user.profile_user
    if request.method == 'POST':
        form = ShippingInfoEditForm(request.POST)
        if form.is_valid():
            profile.phone_number = form.cleaned_data['phone_number']
            profile.shipping_address = form.cleaned_data['shipping_address']
            profile.postal_code = form.cleaned_data['postal_code']
            profile.city = form.cleaned_data["city"]
            profile.save()
            order = Order.objects.create(
                profile=profile
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"]
                )
            cart.clear()
            return render(request, "created_order.html", context={"order": order})
    else:
        form = ShippingInfoEditForm()
    return render(request, "create_order.html", context={"cart": cart, "form": form})