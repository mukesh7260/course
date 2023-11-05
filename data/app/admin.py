from django.contrib import admin
from app.models import Course 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name','course_details','lecture_details','rating','price','image','sold']
    

