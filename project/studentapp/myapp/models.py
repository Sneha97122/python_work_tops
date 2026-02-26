from django.db import models

# Create your models here.

class Dept(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class StudentId(models.Model):
    stid=models.CharField(max_length=20)

    def __str__(self):
        return self.stid

class Student(models.Model):
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    student_id=models.ForeignKey(StudentId,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    age=models.IntegerField()

class Subject(models.Model):
    name=models.CharField(max_length=20)

class Marks(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.FloatField()