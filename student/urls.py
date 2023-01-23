from django.urls import path
from .views import StudentDetail,StudentList

urlpatterns=[
    path("students/",StudentList.as_view(),name="student_list"),
    path("student/<int:pk>/", StudentDetail.as_view(), name="student_detail")
]