from django import forms
from .models import Course,SecClass
# from bootstrap_datepicker_plus import DatePickerInput

class AddCourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('courseCode','courseName','courseIC','midsemDateTime','compreDateTime')
		# widgets = {
        #     'midsemDateTime': DatePickerInput(), # default date-format %m/%d/%Y will be used
        #     'compreDateTime': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        # }



class AddSectionForm(forms.ModelForm):

	class Meta:
		model = SecClass
		fields=('name', 'course', 'secType','days','instructor','startTime','endTime')




