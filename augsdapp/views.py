from django.shortcuts import render
from .forms import AddCourseForm

def homepage(request):
    return render(request, 'augsdapp/homepage.html', {})

def AddCourse(request):
	form = AddCourseForm()
	return render(request, 'augsdapp/AddCourse.html', {'form':form})

def ModifyCourse(request):
    return render(request, 'augsdapp/ModifyCourse.html', {})

def DeleteCourse(request):
    return render(request, 'augsdapp/DeleteCourse.html', {})
