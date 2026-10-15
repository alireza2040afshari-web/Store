from django.shortcuts import render
import re
from .models import ProductModel 

# Create your views here.

def productList(request):
    products = ProductModel.objects.all()

    return render(
        request,
        "store/product.html",
        {"products": products}
    )

def homeView(request):
    products = ProductModel.objects.all()[:3]

    return render(
        request,
        "store/home.html",
        {"products": products}
    )

def detailView(request):
    products = ProductModel.objects.all()
    return render(
        request,
        "store/detail.html",
        {"products":products}
    )