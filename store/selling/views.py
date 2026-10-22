from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductModel , NewsModel , CartModel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction

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


@login_required(login_url='/login/')
@require_POST
def addToCartView(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)

    cart_item, created = CartModel.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save(update_fields=["quantity"])

    return redirect("cart")


@login_required
def cartView(request):
    cart_items = CartModel.objects.filter(
        user=request.user
    ).select_related("product")

    context = {
        "cart_items": cart_items,
    }

    return render(request, "store/cart.html", context)



@login_required
@require_POST
def removeFromCartView(request, item_id):
    cart_item = get_object_or_404(
        CartModel,
        id=item_id,
        user=request.user
    )

    cart_item.delete()

    return redirect("cart")
    