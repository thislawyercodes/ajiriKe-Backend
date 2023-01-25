from django.urls import path
from .views import StudentDetail,StudentList,CreateEducation,EducationList
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='InternKE API')


urlpatterns=[
    # path(r'swagger-docs/',SwaggerSchemaView.as_view(),"swagger-doc"),
    # path("users/", UserCreate.as_view(), name="user_create"),
    path("students/",StudentList.as_view(),name="student_list"),
    path("student/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
    path("education/create",CreateEducation.as_view(),name="create_education"),
    path("education/view",EducationList.as_view(),name="create_education")

]