from django.db import models
from django.db.models.fields import DateField

class Courses(models.Model): 
    #Small inforamation about Course
    name = models.CharField(max_length=100)
    price = models.IntegerField() 

    def __str__(self): 
        return self.name
class Teacher(models.Model):  
    #Small information about Teacher
    full_name = models.CharField(max_length=50) 
    telephone_number = models.CharField(max_length=30, blank=True)  
    
    def __str__(self): 
        return self.full_name

class Student(models.Model):  
    #Information about Student
    full_name = models.CharField(max_length=100) 
    gender = models.CharField(max_length=10, choices=(("Male", "Male"), ("Female", "Female"))) 
    telephone_number =  models.CharField(max_length=30)   
    extra_telephone_number =  models.CharField(max_length=30, blank=True)  
    status = models.CharField(max_length=10, choices=(("New", "New"), ("Loyal", "Loyal")))  

    def __str__(self): 
        return self.full_name 

class Contract(models.Model): 
    # Contract between student and learning center  
    coursetime = (
        ("08:00-10:00", "08:00-10:00"),
        ("10:00-12:00", "10:00-12:00"),
        ("14:00-16:00", "14:00-16:00"),
        ("16:00-18:00", "16:00-18:00"),
        ("18:00-20:00", "18:00-20:00"),
    ) 

    coursedays = (
        ("Monday-Friday", "Monday-Friday"), 
        ("Monday-Wednesday-Friday", "Monday-Wednesday-Friday"), 
        ("Tuesday-Thursday-Saturday", "Tuesday-Thursday-Saturday"), 
        ("Monday-Saturday","Monday-Saturday")
    )
    contract_number = models.PositiveSmallIntegerField(unique=True) 
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True) 
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)  
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)  
    course_days = models.CharField(max_length=100, choices=coursedays)
    course_time =  models.CharField(max_length=30, choices=coursetime)
    group_name = models.CharField(max_length=30)
    # contract_make = Person who make contract with student(ex. Receptionist=Mike)
    contract_maker = models.CharField(max_length=30)
    first_lesson_day = models.DateField()
    status = models.CharField(max_length=15, choices=(("Active", "active"), ("Passive", "Passive")))
    
    def __str__(self): 
        return f"#{self.contract_number}:{self.student} "