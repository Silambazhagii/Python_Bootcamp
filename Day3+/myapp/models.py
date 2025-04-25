from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)  
    description = models.TextField()          
    duration = models.IntegerField()          

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)           
    email = models.EmailField()                       
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()