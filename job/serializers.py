from rest_framework import serializers
from .models import JobPreferences

class JobPreferencesSerializer(serializers.ModelSerializer):
    model=JobPreferences
    fields="__all__"
    