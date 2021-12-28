from rest_framework import generics 
from .models import Student , Contract, Courses, Teacher
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import StudentSerializer, TeacherSerializer, ContractSerializer, CoursesSerializer
class ContractListCreateView(generics.ListCreateAPIView): 
    queryset = Contract.objects.all() 
    serializer_class = ContractSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["contract_number", ]
    ordering_fields = ["contract_number", ]  
class ContractUpdateView(generics.RetrieveUpdateAPIView): 
    queryset = Contract.objects.all() 
    serializer_class = ContractSerializer   
class StudentListCreateView(generics.ListCreateAPIView): 
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["full_name", "status", ]
    ordering_fields = ["full_name", ]  
class StudentUpdateView(generics.RetrieveUpdateAPIView): 
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer   
class StudentDeleteView(generics.RetrieveDestroyAPIView): 
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer  
class TeacherListCreateView(generics.ListCreateAPIView): 
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["full_name", ]
    ordering_fields = ["full_name", ] 

class TeacherUpdateView(generics.RetrieveUpdateAPIView): 
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer     

class TeacherDeleteView(generics.RetrieveDestroyAPIView): 
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer   
class CourseListCreateView(generics.ListCreateAPIView): 
    queryset = Courses.objects.all() 
    serializer_class = CoursesSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["name", ]
    ordering_fields = ["name", ] 
class CourseUpdateView(generics.RetrieveUpdateAPIView): 
    queryset = Courses.objects.all() 
    serializer_class = CoursesSerializer 
class CourseDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Courses.objects.all() 
    serializer_class = CoursesSerializer  