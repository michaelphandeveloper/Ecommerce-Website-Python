from django.db import models
from .models import Category

# Product
class Product(models.Model):
    image = models.ImageField()
    details = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.ForeignKey(Category,on_delete=models.CASCADE)
    size = models.ForeignKey(Category,on_delete=models.CASCADE)
    materials = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.title


