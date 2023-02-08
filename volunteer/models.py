from django.db import models

class Volunteer(models.Model):
    job_title=models.CharField(max_length=100)
    job_types=models.CharField(max_length=100)
    work_environment=models.CharField(max_length=100)
    
