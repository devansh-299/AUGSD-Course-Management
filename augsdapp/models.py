from django.db import models
from django.conf import settings
from django.utils import timezone


class Course(models.Model):
    CourseCode = models.CharField(max_length=10)
    CourseName = models.CharField(max_length=100)
    MidsemDateTime = models.DateTimeField()
    CompreDateTime = models.DateTimeField()
    courseIC = models.CharField(max_length=50)
    Sections=models.IntegerField()


# class Sections(models.Model):
#     CourseCode=models.ForeignKey(Courses,)




# class Instructor(models.Model):
#     name = models.CharField(max_length = 100)


# class SubSection(models.Model):
#     Instructors = models.ForeignKey(Instructor, related_name='subSection1', default=None)   
#     instructor2 = models.ForeignKey(Instructor, related_name='subSection2', default=None)   
#     days = models.CharField(max_length = 7)
#     startTime = models.IntegerField()
#     endTime = models.IntegerField()
#     # room = models.ForeignKey(Room, related_name='room', default=None)
#     courseCode = models.CharField(max_length = 10)





