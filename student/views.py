from django.shortcuts import render
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404


class StudentList(APIView):
    def get(self,request):
        students=Student.objects.all()
        data=StudentSerializer(students,many=True).data
        return Response(data) 
    
class StudentDetail(APIView):
    def get(self, request, pk):
        students = get_object_or_404(Student, pk=pk)
        data = StudentSerializer(students).data
        return Response(data)
          
