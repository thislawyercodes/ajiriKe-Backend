from django.db import models

# Create your models here.
class JobPreferences(models.Model):
    job_title=models.CharField(max_length=100,blank=True)
    job_types=models.CharField(max_length=100,blank=True)
    work_environment=models.CharField(max_length=100,blank=True)
    