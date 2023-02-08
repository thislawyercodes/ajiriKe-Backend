from django.urls import path
from .views import CreateEducation,EducationList

app_name="education"
urlpatterns=[
    path("education/create",CreateEducation.as_view(),name="create_education"),
    path("education/view",EducationList.as_view(),name="create_education")
]