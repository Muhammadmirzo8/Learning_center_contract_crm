
from rest_framework import serializers 
from .models import Student , Contract, Courses, Teacher 

class CoursesSerializer(serializers.ModelSerializer): 
    # Serilizer for Courses model
    class Meta: 
        model = Courses 
        fields = ("name", "price")  

class StudentSerializer(serializers.ModelSerializer):  
    # Serilizer for Student model
    class Meta: 
        model = Student
        fields = ("full_name", "gender", "telephone_number", "extra_telephone_number", "status")   

class TeacherSerializer(serializers.ModelSerializer):  
    # Serilizer for Teacher model
    class Meta: 
        model = Teacher
        fields = ("full_name", "telephone_number")  
    
class ContractSerializer(serializers.ModelSerializer):  
    # Serilizer for Contract model
    class Meta: 
        model = Contract 
        fields = (" contract_number", "student", 
                        "teacher", "course", 
                      "course_days", "course_time", 
                     "group_name", "contract_maker", 
                     "first_lesson_day", "status" ) 

