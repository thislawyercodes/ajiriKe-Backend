from django.urls import path
from .views import StudentDetail,StudentList
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

app_name="student"

urlpatterns=[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("list/",StudentList.as_view(),name="student_list"),
    path("list/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
]