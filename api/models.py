from django.db import models
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(blank=False,unique=True)
    city=models.CharField(max_length=300,blank=False,default=True)
    location=PlainLocationField(based_fields=['city'],zoom=7,blank=False)
    phone_number=PhoneNumberField(null=False,blank=False,unique=True)
    resume=models.FileField(blank=False,upload_to='uploads')
    cover_letter=models.FileField(blank=False,upload_to='uploads')
    #education=models.ForeignKey(Education,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
     
class Education(models.Model):
    academic_transcripts=models.URLField(blank=True)
    skills=models.TextField(blank=True)
    Licenses=models.FileField(blank=True)
    certifications=models.FileField(blank=True)
    languages=models.CharField(max_length=99,blank=True)
   
    def __str__(self):
       return self.skills
    
class JobPreferences(models.Model):
    job_title=models.CharField(max_length=100,blank=True)
    job_types=models.CharField(max_length=100,blank=True)
    work_environment=models.CharField(max_length=100,blank=True)

class Volunteer(models.Model):
    job_title=models.CharField(max_length=100)
    job_types=models.CharField(max_length=100)
    work_environment=models.CharField(max_length=100)
    


    