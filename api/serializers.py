from rest_framework import serializers
from .models import Student,Education,Volunteer,JobPreferences

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
        
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields="__all__"

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteer
        fields="__all__"
        
class JobPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobPreferences
        fields="__all__"
           
 