from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserCreationForm


def register_view(request):
    if request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("quiz:start_quiz")
    else:
        form = NewUserCreationForm()
    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("quiz:start_quiz")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("user_auth:login")


@login_required
def profile_view(request):
    return render(request, "auth/profile.html")
