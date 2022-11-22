from django.db import models

from django.db import models
from category.models import Category
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    credit = models.IntegerField()
    hour = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.code

