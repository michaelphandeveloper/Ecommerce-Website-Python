from django.db import models

class lastname(models.lastname):
  name = models.NameField(max_length=16)

    class Meta:
        db_table = "lastname"
    def __str__(self):
        return self.title
