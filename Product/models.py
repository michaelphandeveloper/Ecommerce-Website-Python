from django.db import models

# Product
class Product(models.Model):
    image = models.ImageField()
    details = models.TextField()

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.title

# Brand
class Brand(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="brand_imgs/")

    class Meta:
        db_table = "Brand"

    def __str__(self):
        return self.title

# Color
class Color(models.Model):
    title = models.CharField(max_length=50)
    color_code = models.CharField(max_length=20)

    class Meta:
        db_table = "Color"

    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "Size"

    def __str__(self):
        return self.title

# Price
class Price(models.Model):
    title = models.FloatField(max_length=20)

    class Meta:
        db_table = "Price"

    def __str__(self):
        return self.title

#Materials
class Materials(models.Model):
    description = models.Model(max_length=50)

    class Meta:
        db_table = "Materials"
    def __str__(self):
        return self.title  
