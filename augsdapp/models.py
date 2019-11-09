from django.db import models
from django.conf import settings
from django.utils import timezone

class Course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=100)
    midsemDateTime = models.DateTimeField()
    compreDateTime = models.DateTimeField()
    #courseIC = models.ForeignKey(Instructor,related_name="InstructorIncharge",default=None)
    def __str__(self):
        return self.courseCode


