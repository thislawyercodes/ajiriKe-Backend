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
     


    