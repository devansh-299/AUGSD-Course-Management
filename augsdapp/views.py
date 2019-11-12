from django.shortcuts import render, redirect
from .forms import AddCourseForm,AddSectionForm

def homepage(request):
    return render(request, 'augsdapp/homepage.html', {})

def AddCourse(request):
	if request.method =="POST":
		form = AddCourseForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			return redirect('AddSection')
	else:
		form = AddCourseForm()
	return render(request, 'augsdapp/AddCourse.html', {'form':form})

def AddSection(request):
	if request.method=="POST":
		form = AddSectionForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()
			return redirect('AddCourse')
	else:
		form=AddSectionForm()
	return render(request,'augsdapp/AddSection.html',{'form':form})

def ModifyCourse(request):
    return render(request, 'augsdapp/ModifyCourse.html', {})

def DeleteCourse(request):
    return render(request, 'augsdapp/DeleteCourse.html', {})