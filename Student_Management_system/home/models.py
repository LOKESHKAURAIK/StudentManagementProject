from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    is_active =models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    course_name=models.CharField(max_length=50)
    course_fees=models.FloatField()
    course_duration=models.FloatField()
    course_text=models.TextField()
    is_active =models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    mobile=models.IntegerField()
    college=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    is_active =models.BooleanField(default=True)
    Std_course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def _str_(self):
        return self.name


class Teacher(models.Model):
    t_name=models.CharField(max_length=50)
    t_email=models.EmailField(max_length=254)
    t_mobile=models.IntegerField((""))
    t_joining=models.IntegerField((""))
    t_education=models.CharField(max_length=50)
    t_id=models.CharField(max_length=50)
    t_experience=models.IntegerField((""))
    t_package=models.IntegerField((""))
    def _str_(self):
        return self.t_name
