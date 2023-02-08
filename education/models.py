from django.db import models

# Create your models here.
class Education(models.Model):
    academic_transcripts=models.URLField(blank=True)
    skills=models.TextField(blank=True)
    Licenses=models.FileField(blank=True)
    certifications=models.FileField(blank=True)
    languages=models.CharField(max_length=99,blank=True)
   
    def __str__(self):
       return self.skills
    