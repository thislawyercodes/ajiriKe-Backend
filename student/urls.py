from django.urls import path
from .views import StudentController
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
   path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
   path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
   path("register/",StudentController.as_view(),name="register_student"),
   path("list/<int:pk>/", StudentController.as_view(), name="get_student_detail"),
   path("list/", StudentController.as_view(), name="get_students"),
   path("edit/<int:pk>/",StudentController.as_view(),name="edit_student"),
   path("delete/<int:pk>/",StudentController.as_view(),name="delete_student"),
]