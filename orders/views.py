from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.cart import Cart
from .models import Order, OrderProduct
from profiles.forms import ShippingOrderEditForm


@login_required(login_url="login")
def create_order(request):
    cart = Cart(request)
    profile = request.user.profile_user
    if request.method == "POST":
        form = ShippingOrderEditForm(request.POST)
        if form.is_valid():
            profile.phone_number = form.cleaned_data["phone_number"]
            profile.shipping_address = form.cleaned_data["shipping_address"]
            profile.postcode = form.cleaned_data["postcode"]
            profile.city = form.cleaned_data["city"]
            profile.save()

            order = Order.objects.create(
                profile=profile
            )
            for item in cart:
                OrderProduct.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"]
                )
            cart.clear()
            return render(request, "created.html", context={"order": order})
    else:
        form = ShippingOrderEditForm()
    return render(request, "create.html", context={"cart": cart, "form": form})



