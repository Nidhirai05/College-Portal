from django.db import models
from django.utils import timezone

# Create your models here.
#Notice Model

class Notice(models.Model):
    contents=models.CharField(max_length=100)
    date=models.DateField(default=timezone.now) #todays date

    
    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.contents

#feedback Model

class Feedback(models.Model):
    name=models.CharField(max_length=45,default="guest",null=True,blank=True)
    email=models.EmailField(max_length=50)
    rating=models.CharField(max_length=5,default="5")
    remarks=models.TextField()
    date=models.DateField(default=timezone.now)

    
    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.name


#Contact Model

class Contact(models.Model):
    name=models.CharField(max_length=45,default="guest",null=True,blank=True)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    query=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.name


class Consultancy(models.Model):
    id=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    cname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    work_area=models.TextField()
    address=models.TextField()

    
    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.cname

#event model

class Event(models.Model):
    event_name=models.CharField(max_length=70)
    event_venue=models.TextField(default="College Campus")
    event_organizer=models.CharField(max_length=50,default="College")
    event_description=models.TextField()
    event_date=models.DateField(default=timezone.now) 
    event_pic=models.ImageField(max_length=100,upload_to="college_app/event_images",default=" ") 

    
    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.event_name


class Alumni(models.Model):
    name=models.CharField(max_length=70)
    course=models.CharField(max_length=50)
    completion_year=models.CharField(max_length=50)
    photo=models.ImageField(max_length=100,upload_to="college_app/alumni_images",default=" ") 
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

    
    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.name

#outside Alumni class
gender=(('','Select Gender'),("M","Male"),("F","Female"),)

class Student(models.Model):
    id=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=70)
    course=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)  
    gender=models.CharField(max_length=6,choices=gender) 
    address=models.TextField()
    student_pic=models.ImageField(max_length=100,upload_to="college_app/student_images",default=" ")   

    
    def __str__(self):   #we are overriding the method-> It is used to represent object in the form of string
        return self.name