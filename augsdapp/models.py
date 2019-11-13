from django.db import models
from django.conf import settings
from django.utils import timezone


class Course(models.Model):
    courseCode = models.CharField(max_length=10,unique=True)
    courseName = models.CharField(max_length=100)
    midsemDateTime = models.DateTimeField(unique=True)
    compreDateTime = models.DateTimeField(unique=True)
    courseIC = models.ForeignKey(settings.AUTH_USER_MODEL,
    	on_delete="SET_NULL",
    	null=True)

    def __str__(self):
    	return "(" + str(self.courseCode) + ") - " + \
    			str(self.courseName)


class Room(models.Model):
	location = models.CharField(max_length=10)


secClassChoices = (
	('L', "Lecture"),
	('T', "Tutorial"),
	('P', "Practical"))

class SecClass(models.Model):
    course = models.ForeignKey(Course,
      	on_delete=models.CASCADE,
      	null=True)
    name = models.CharField(max_length=2,
    	help_text="L2, T3, P2, or other relevant name")
    secType = models.CharField(max_length=1,choices=secClassChoices)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL,
    	on_delete="SET_NULL",
    	null=True)
    days = models.CharField(max_length=7)
    startTime = models.TimeField()
    endTime = models.TimeField()
    room = models.ForeignKey(Room,
    	on_delete=models.SET_NULL,null=True)


