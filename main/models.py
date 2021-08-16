from django.db import models

# Create your models here.

class School(models.Model):
    School = models.CharField(max_length=50)

class Admin(models.Model):
    Full_name = models.CharField(max_length=50)
    User_name = models.CharField(max_length=20,unique=True)
    Password = models.CharField(max_length=15)
    school = models.ForeignKey(School,on_delete=models.CASCADE)

class Course(models.Model):
    Course_title = models.CharField(max_length=30)
    school = models.ForeignKey(School,on_delete=models.CASCADE)

class Student(models.Model):
    Full_name = models.CharField(max_length=50)
    User_name = models.CharField(max_length=20,unique=True)
    Password = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
