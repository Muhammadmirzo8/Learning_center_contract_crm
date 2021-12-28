
from rest_framework import serializers 
from .models import Student , Contract, Courses, Teacher 

class CoursesSerializer(serializers.ModelSerializer): 
    # Serilizer for Courses model
    class Meta: 
        model = Courses 
        fields = ("id", "name", "price")  

class StudentSerializer(serializers.ModelSerializer):  
    # Serilizer for Student model
    class Meta: 
        model = Student
        fields = ("id", "full_name", "gender", "telephone_number", "extra_telephone_number", "status")   

class TeacherSerializer(serializers.ModelSerializer):  
    # Serilizer for Teacher model
    class Meta: 
        model = Teacher
        fields = ("id", "full_name", "telephone_number")  
    
class ContractSerializer(serializers.ModelSerializer):  
    # Serilizer for Contract model 
    teacher= serializers.SlugField(read_only=True) 
    student = serializers.SlugField(read_only=True) 
    course= serializers.SlugField(read_only=True)
    class Meta: 
        model = Contract 
        fields = ("id","contract_number", "student", 
                        "teacher", "course", 
                      "course_days", "course_time", 
                     "group_name", "contract_maker", 
                     "first_lesson_day", "status" ) 

