from django.db import models

# Create your models here.
class student(models.Model):
    stuname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class employee(models.Model):
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dept = models.CharField(max_length=500)

class commite(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=500) 
