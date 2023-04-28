from django.db import models


class StudentsData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
    iname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
