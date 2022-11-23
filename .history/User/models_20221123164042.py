from django.db import models

class lastname(models.lastname):
  lastname = models.NameField(max_length=16)
  class Meta:
        db_table = "lastname"

    def __str__(self):
        return self.title

class firstname(models.firstname):
  firstname = models.NameField(max_length=16)

class phone(models.phone):
  phone = models.FloatField(max_length=11)

class email(models.email):
  email = models.EmailField(max_length=25)

class gender(models.gender):
  gender = models.TextField(max_length=8)

class address(models.address):
  address = models.CharField(max_length=25)  

