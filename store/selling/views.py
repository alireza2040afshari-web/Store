from django.shortcuts import render
import re
from .models import ProductModel

# Create your views here.
def homeView(request):
    return render(request, "store/home.html")

def productList(request):
    products = ProductModel.objects.all()
    return render(request, "store/product.html", {"products": products})