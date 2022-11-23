from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name