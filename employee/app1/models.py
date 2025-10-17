from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id=models.CharField(max_length=100)
    emp_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    designation=models.CharField(max_length=50)
    salary = models.IntegerField()
    image=models.ImageField(upload_to="employee")