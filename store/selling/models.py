from django.db import models
from django.conf import settings

class ProductModel (models.Model):
    name = models.CharField( max_length=50)
    factory = models.CharField( max_length=50)
    origin = models.CharField( max_length=50)
    description = models.TextField()
    poster = models.ImageField(upload_to='productImage/', null=True)

    def __str__(self):
        return self.name

class PriceModel (models.Model):
    price = models.IntegerField()
    discount = models.IntegerField()
    productModel = models.ForeignKey("ProductModel", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.price)

class StockModel (models.Model):
    stock = models.IntegerField()
    productModel = models.ForeignKey("ProductModel", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.stock)


class NewsModel (models.Model):
    poster = models.ImageField(upload_to='productImage/', null=True)
    name = models.CharField( max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
            return self.name


class CartModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "product"],
                name="unique_user_cart_product"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
