from django.shortcuts import render
from rest_framework.decorators import api_view 
from app.models import Course 
from app.serializers import CourseSerializer 
from rest_framework.response import Response 

@api_view(['GET'])
def get(request):
    course = Course.objects.all()
    courses = {"coursp":course}
    return render(request,'index.html',courses) 


@api_view(['POST'])
def create(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"created-data":serializer.data})
    return Response(serializer.errors)