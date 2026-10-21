# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.models import ProfileModel
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


def loginView(request):

    # POST
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)

            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        else:
            context = {
                "username": username,
                "errorMessage": "Not Found"
            }

            return render(request, "account/login.html", context)

    # GET
    else:
        return render(request, "account/login.html", {})


def registerView(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        with transaction.atomic():
            user = form.save()

            ProfileModel.objects.create(
                user=user,
                status=1,
                credit=0
            )

            login(request, user)
            return redirect("profile")

    return render(request, "account/register.html", {"form": form})


def logoutView(request):
    logout(request)
    return redirect("home")


@login_required
def profileView(request):
    profile, created = ProfileModel.objects.get_or_create(
        user=request.user,
        defaults={
            "status": 1,
            "credit": 0,
        }
    )

    context = {
        "profile": profile,
        "date_join": request.user.date_joined.strftime("%Y-%m-%d")
    }

    return render(request, "account/profile.html", context)