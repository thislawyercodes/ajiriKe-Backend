from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    date_of_birth=models.PositiveSmallIntegerField()
    # experience_field=models.Choices()
    academic_transcripts=models.URLField()
    
    # def __str__(self):
    #     return self.first_name
    