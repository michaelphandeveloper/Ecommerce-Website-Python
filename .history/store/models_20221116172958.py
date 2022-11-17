from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  slug = models.SlugField(max_length=255, db_index=True)
