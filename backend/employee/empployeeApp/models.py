from django.db import models

# Create your models here.
class Employee(models.Model):
  Ename=models.CharField(max_length=50)
  department=models.CharField(max_length=50)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  