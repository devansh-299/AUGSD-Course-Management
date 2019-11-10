from django.shortcuts import render

def homepage(request):
    return render(request, 'augsdapp/homepage.html', {})

def AddCourse(request):
    return render(request, 'augsdapp/AddCourse.html', {})

def ModifyCourse(request):
    return render(request, 'augsdapp/ModifyCourse.html', {})

def DeleteCourse(request):
    return render(request, 'augsdapp/DeleteCourse.html', {})
