# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings


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


def logoutView(request):
    logout(request)
    return redirect("home")