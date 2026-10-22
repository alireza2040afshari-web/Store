"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from selling.views import homeView, productList, detailView, cartView, addToCartView, removeFromCartView
from accounts.views import logoutView, loginView, profileView
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import registerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('productList/', productList, name='products'),
    path('detail/<int:product_id>', detailView,name='details'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('accounts/profile/', profileView, name='profile'),
    path("register/", registerView, name="register"),
    path("cart/", cartView,name="cart"),
    path("cart/add/<int:product_id>/", addToCartView, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", removeFromCartView, name="remove_from_cart")
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)