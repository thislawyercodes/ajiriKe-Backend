from django.urls import path
from .views import StudentController,EducationController
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="InternKe API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

app_name="api"

urlpatterns=[
   path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
   path("student/register/",StudentController.as_view(),name="register_student"),
   path("student/list/<int:pk>/", StudentController.as_view(), name="get_student_detail"),
   path("student/list/", StudentController.as_view(), name="get_students"),
   path("student/edit/<int:pk>/",StudentController.as_view(),name="edit_student"),
   path("student/delete/<int:pk>/",StudentController.as_view(),name="delete_student"),
   path("education/register/",EducationController.as_view(),name="register_education"),
   path("education/list/<int:pk>/",EducationController.as_view(), name="get_education_detail"),
   path("education/list/", EducationController.as_view(), name="get_education_list"),
   path("education/edit/<int:pk>/",EducationController.as_view(),name="edit_education"),
   path("education/delete/<int:pk>/",EducationController.as_view(),name="delete_education"),
]