from rest_framework import serializers 
from app.models import Course 

class CourseSerializer(serializers.ModelSerializer):
    class Meta :
        model = Course
        fields = ['course_name','course_details','lecture_details','rating','price','image','sold']