from django.db import models

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