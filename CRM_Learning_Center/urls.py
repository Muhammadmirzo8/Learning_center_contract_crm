
from django.contrib import admin
from django.urls import path
from CRM.views import * 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
from rest_framework.permissions import AllowAny

doc_view = get_schema_view(
     openapi.Info(
         title="CRM", 
         default_version = 'v1', 
         descrption = '(REST API) CRM', 
         contact = openapi.Contact("Muhammadmirzo Toshpolatjonov <mtoshpulatjonov@gmail.com>")
     ), 
     public=True, 
     permission_classes=(AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls), 

    path('contract/', ContractListCreateView.as_view(), name="contract"),
    path('contract/update/<int:pk>', ContractUpdateView.as_view(), name="contract-update"), 

    path('student/', StudentListCreateView.as_view(), name='student'),  
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name="student-update"), 
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name="student-delete"), 
    

    path('teacher/', TeacherListCreateView.as_view(), name='teacher'), 
    path('teacher/update/<int:pk>', TeacherUpdateView.as_view(), name="teacher-update"),  
    path('teacher/delete/<int:pk>', TeacherDeleteView.as_view(), name="teacher-delete"),

    path('course/', CourseListCreateView.as_view(), name="course"), 
    path('course/update/<int:pk>', CourseUpdateView.as_view(), name="course-update"), 
    path('course/delete/<int:pk>', CourseDeleteView.as_view(), name="course-delete"), 

    path("", doc_view.with_ui('swagger', cache_timeout=0), name="swagger_doc") ,


]
