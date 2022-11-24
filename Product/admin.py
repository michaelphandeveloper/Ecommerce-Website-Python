from django.contrib import admin
from .models import Product
from .models import ProductAttribute

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'color', 'size', 'material')

admin.site.register(Product, ProductAdmin)

#Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'price')
admin.site.register(ProductAttribute, ProductAttributeAdmin)