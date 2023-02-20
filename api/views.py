from .models import Student,Education,Volunteer,JobPreferences
from .utils import BaseCRUDAPIController
from .serializers import StudentSerializer,EducationSerializer,VolunteerSerializer,JobPreferencesSerializer


class StudentController(BaseCRUDAPIController):
    model=Student
    serializer=StudentSerializer

class EducationController(BaseCRUDAPIController):
    model=Education
    serializer=EducationSerializer

class VolunteerController(BaseCRUDAPIController):
    model=Volunteer
    serializer=VolunteerSerializer

class JobPreferencesController(BaseCRUDAPIController):
    model=JobPreferences
    serializer=JobPreferencesSerializer

          
