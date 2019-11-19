from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Course(models.Model):
    courseCode = models.CharField(max_length=10, unique=True)
    courseName = models.CharField(max_length=100)
    midsemDateTime = models.DateTimeField(unique=True)
    compreDateTime = models.DateTimeField(unique=True)
    courseIC = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete="SET_NULL",
        null=True)

    def __str__(self):
        return "(" + str(self.courseCode) + ") - " + str(self.courseName)


class Room(models.Model):
    name = models.CharField(
        max_length=10,
        help_text="LT-1,C-301,A-501,DLT-5",
        unique=True,
        default='LT-1')
    capacity = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)


class Instructor(models.Model):
    instructorId = models.OneToOneField(User, on_delete=models.CASCADE)
    days = models.CharField(max_length=7, null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return str(self.instructorId)


class SecClass(models.Model):

    secClassChoices = (
        ('L', "Lecture"),
        ('T', "Tutorial"),
        ('P', "Practical"))

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True)
    name = models.CharField(
        max_length=2,
        help_text="L2, T3, P2, or other relevant name")
    secType = models.CharField(
        max_length=1,
        choices=secClassChoices)
    instructor = models.ForeignKey(
        Instructor,
        on_delete="SET_NULL",
        null=True)
    days = models.CharField(max_length=7)
    startTime = models.TimeField()
    endTime = models.TimeField()
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True)
    classSize = models.IntegerField(
        help_text="Approximate number of students in class",
        null=True)
