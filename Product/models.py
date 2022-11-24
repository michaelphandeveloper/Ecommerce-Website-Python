from django.db import models
from Category.models import Category, Brand, Color, Size, Material

# Product
class Product(models.Model):
    title = models.CharField(max_length=25, null=True)
    image = models.ImageField(upload_to="product_imgs/")
    details = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.title

# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
         return self.product.title