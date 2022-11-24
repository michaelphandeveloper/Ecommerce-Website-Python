from django.db import models

from Category.models import Category, Brand, Color, Size, Material


# Product
class Product(models.Model):
    image = models.ImageField(upload_to="product_imgs/")
    details = models.TextField()
    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.title


