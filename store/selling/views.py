from django.shortcuts import render
from .models import ProductModel


def homeView(request):
    return render(request, "store/home.html")


def productList(request):
    products = ProductModel.objects.all()

    return render(
        request,
        "store/products.html",
        {"products": products}
    )