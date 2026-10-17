from django.shortcuts import render, get_object_or_404
from .models import ProductModel , NewsModel

# Create your views here.

def productList(request):
    products = ProductModel.objects.all()

    return render(
        request,
        "store/product.html",
        {"products": products}
    )


def homeView(request):
    news = NewsModel.objects.all().order_by('-id')[:3]

    return render(request, "store/home.html", {
        "news": news
    })


def detailView(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)

    return render(
        request,
        "store/detail.html",
        {"product": product}
    )