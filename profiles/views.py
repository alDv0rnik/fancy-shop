from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUserForm


def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        # breakpoint()
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                messages.info(
                    request, f"The user with username {username} already exists"
                )
            else:
                form.save()
                messages.info(request, f"The user {username} has been registered")
                return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'register_user.html', context=context)