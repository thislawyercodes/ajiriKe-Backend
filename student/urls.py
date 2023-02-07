from django.urls import path
from .views import StudentDetail,StudentList,CreateEducation,EducationList
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="InternKe API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns=[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("list/",StudentList.as_view(),name="student_list"),
    path("list/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
    path("education/create",CreateEducation.as_view(),name="create_education"),
    path("education/view",EducationList.as_view(),name="create_education")
]