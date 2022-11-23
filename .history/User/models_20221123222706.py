from django.db import models

class lastname(models.Model):
  lastname = models.NameField(max_length=16)

class firstname(models.Model):
  firstname = models.NameField(max_length=16)

class phone(models.Model):
  phone = models.FloatField(max_length=11)

class email(models.Model):
  email = models.EmailField(max_length=25)

class gender(models.Model):
  gender = models.TextField(max_length=8)

class address(models.address):
  address = models.CharField(max_length=25)  

