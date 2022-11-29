from django.db import models

# Banner
class Banner(models.Model):
    img = models.CharField(max_length=50)
    alt_text = models.CharField(max_length=75)
    
# Category

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.title

# Brand

class Brand(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="brands_imgs/")

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

# Material

class Material(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "Material"
    
    def __str__(self):
        return self.title