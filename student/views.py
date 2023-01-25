from django.shortcuts import render
from .models import Student,Education
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer,EducationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework_swagger import renderers
from rest_framework.schemas import SchemaGenerator



# class UserCreate(APIView):
#     def post(self,request):
#         dat
class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema) 
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