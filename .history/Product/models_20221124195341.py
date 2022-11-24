from django.db import models

# Product
class Product(models.Model):
    image = models.ImageField(upload_to="product_imgs/")
    details = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    materials = models.ForeignKey(Material,on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.title


