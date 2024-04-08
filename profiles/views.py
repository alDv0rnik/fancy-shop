import logging

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from catalog.models import Product
from .forms import CreateUserForm, UserEditForm, ProfileEditForm

from .decorators import unauthenticated_user
from .models import Profile

logger = logging.getLogger('fancy-shop-logger')


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                logger.warning(f"The user with username {username} already exists")
                messages.info(
                    request, f"The user with username {username} already exists"
                )
            else:
                form.save()
                logging.info(f"The user {username} has been registered")
                messages.info(request, f"The user {username} has been registered")
                return redirect("login")
    context = {
        "form": form
    }
    return render(request, 'register_user.html', context=context)


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            logger.warning("Login or password do not match")
            messages.info(request, "Login or password do not match")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def get_profile_details(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)

    context = {
        "profile": profile
    }
    return render(request, 'profile.html', context=context)


@login_required(login_url="login")
def edit_profile_details(request, profile_slug):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=request.user.profile_user
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            logger.info(f"Profile for user {request.user.username} has been updated")
            messages.info(request, "Your profile has been updated")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile_user)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, "profile_edit.html", context=context)


def add_to_favourites(request, profile_slug, product_id):
    product = Product.objects.get(pk=product_id)
    profile = request.user.profile_user
    if profile.favourites.filter(pk=product_id).exists():
        profile.favourites.remove(product)
    else:
        profile.favourites.add(product)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def get_favourites_list(request, profile_slug):
    profile = request.user.profile_user
    products_list = profile.favourites.all()
    paginator = Paginator(products_list, 3)
    page_number = request.GET.get("page", 1)
    products = paginator.page(page_number)
    context = {
        "products": products
    }
    return render(request, "favourites.html", context=context)