from .models import Student
from .utils import BaseCRUDAPIController
from .serializers import StudentSerializer


class StudentController(BaseCRUDAPIController):
    model=Student
    serializer=StudentSerializer
    

          
