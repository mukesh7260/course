from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=255,null=True,blank=True)
    course_details = models.CharField(max_length=255,null=True, blank=True)
    lecture_details = models.CharField(max_length=255,null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='media',null=True, blank=True)
    sold = models.BooleanField(default=False,null=True,blank=True)


    
   