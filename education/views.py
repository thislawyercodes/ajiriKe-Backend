from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EducationSerializer
from .models import Education

class CreateEducation(APIView):
    def post(self,request):
        data= EducationSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data)
        else:
            return ("error")
        
class EducationList(APIView):
    def get(self,request):
        education=Education.objects.all()
        data=EducationSerializer(education,many=True).data 
        return Response(data)