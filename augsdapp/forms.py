from django import forms
from .models import Course,SecClass
from bootstrap_datepicker_plus import DateTimePickerInput, TimePickerInput

class AddCourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('courseCode','courseName','courseIC','midsemDateTime','compreDateTime')
		widgets = {
			'midsemDateTime':DateTimePickerInput(),
			'compreDateTime':DateTimePickerInput()
		}




class AddSectionForm(forms.ModelForm):

	class Meta:
		model = SecClass
		fields=('name', 'course', 'secType','days','instructor','classSize','room','startTime','endTime')
		widgets = {
			'startTime':TimePickerInput(),
			'endTime':TimePickerInput()
		}

