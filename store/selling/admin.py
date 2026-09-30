from django.contrib import admin
from selling.models import ProductModel , PriceModel , StockModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(PriceModel)
admin.site.register(StockModel)