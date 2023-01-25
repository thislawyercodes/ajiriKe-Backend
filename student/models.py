from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    email=models.EmailField(blank=True)
    location=models.CharField(max_length=45,blank=True)
    date_of_birth=models.PositiveSmallIntegerField(blank=True)
    phone_number=models.CharField(max_length=15,blank=True)
    resume=models.FileField(blank=True)
    cover_letter=models.FileField(blank=True)
    # education=models.ForeignKey(Education,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
   
   
class Education(models.Model):
    academic_transcripts=models.URLField(blank=True)
    skills=models.TextField(blank=True)
    Licenses=models.FileField(blank=True)
    certifications=models.FileField(blank=True)
    languages=models.CharField(max_length=100,blank=True)
    
    
class JobPreferences(models.Model):
    job_title=models.CharField(max_length=100,blank=True)
    job_types=models.CharField(max_length=100,blank=True)
    work_environment=models.CharField(max_length=100,blank=True)
    
# class Volunteer(models.Model):
#     job_title=models.CharField(max_length=100)
#     job_types=models.CharField(max_length=100)
#     work_environment=models.CharField(max_length=100)
    
    