from django import forms
from .models import Course,SecClass

class AddCourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('courseCode', 'courseIC', 'courseName','midsemDateTime','compreDateTime')


class AddSectionForm(forms.ModelForm):

	class Meta:
		model = SecClass
		fields=('name', 'course', 'secType','days','startTime','endTime')




