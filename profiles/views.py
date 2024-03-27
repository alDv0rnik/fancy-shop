import logging
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CreateUserForm

from .decorators import unauthenticated_user


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
