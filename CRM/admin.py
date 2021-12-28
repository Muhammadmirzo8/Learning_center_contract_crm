from django.contrib import admin
from .models import Student , Contract, Courses, Teacher 

admin.site.register(Student) 
admin.site.register(Courses) 
admin.site.register(Teacher) 
admin.site.register(Contract)
# Register your models here.
