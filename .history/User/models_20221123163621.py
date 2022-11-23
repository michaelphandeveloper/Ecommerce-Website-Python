from django.db import models

class lastname(models.lastname):
  name = models.NameField(max_length=16)

class firstname(models.firstname):
  name = models.NameField(max_length=16)

class phone(models.phone):
  name = models.CharField(max_length=11)

class email(models.email):
  name = models.CharField(max_length=11)

class gender(models.gender):
  name = models.CharField(max_length=11)

class address(models.address):
  name = models.CharField(max_length=11)  

