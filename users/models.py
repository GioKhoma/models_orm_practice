from django.db import models
from django.contrib.auth.models import User

#1
class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} - {self.surname}"
    
class Passport(models.Model):
    passport_number = models.CharField(max_length=255, unique=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()

    citizen = models.OneToOneField(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.passport_number} - {self.citizen}"
    

#2
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} {self.surname}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} : {self.user_profile}"
    


#3
class Student(models.Model):
    person = models.OneToOneField(Passport, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.person}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student, null=True, blank=True)

    def __str__(self):
        return self.title
