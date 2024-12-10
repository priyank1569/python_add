from django.db import models

class StudentModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=30)