from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddCourseForm, AddSectionForm
from .models import SecClass, Course
from django.contrib import messages
from django.db.models import Q


def homepage(request):
    return render(request, 'augsdapp/homepage.html', {})


def AddCourse(request):
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('AddSection', CourseCode=post.courseCode)
    else:
        form = AddCourseForm()
    return render(request, 'augsdapp/AddCourse.html', {'form': form})


def AddSection(request, CourseCode):
    course = get_object_or_404(Course, courseCode=CourseCode)
    print(course.courseCode)
    if request.method == "POST":
        form = AddSectionForm(request.POST)
        if form.is_valid():
            instructorCheck = SecClass.objects.filter(
                startTime__gte=form.cleaned_data.get('startTime'),
                endTime__lte=form.cleaned_data.get('endTime'),
                days=form.cleaned_data.get('days')).count()
            classSize = form.cleaned_data.get('classSize')
            roomSelected = form.cleaned_data.get('room')
            if instructorCheck != 0:
                messages.error(
                    request, 'Instructor not available for' +
                    ' the selected time slot')
                form = AddSectionForm(request.POST)
            elif classSize > roomSelected.capacity:
                messages.error(
                    request, 'Room cannot accomodate more participants')
                form = AddSectionForm(request.POST)
            else:
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Successful')
                return redirect('AddCourse')
    else:
        form = AddSectionForm()
    return render(request, 'augsdapp/AddSection.html',
                  {'form': form, 'course': course}
                  )


def ModifyCourse(request):
    if request.method == "GET":
        search_query = request.GET.get('q', None)
        submitbutton = request.GET.get('submit')
        if search_query is not None:
            lookups = Q(courseCode__icontains=search_query) | \
                Q(courseName__icontains=search_query) | \
                Q(courseIC__username__icontains=search_query)
            results = Course.objects.filter(lookups)
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'augsdapp/ModifyCourse.html', context)
        else:
            messages.success(request, 'No Course Found')
            return render(request, 'augsdapp/ModifyCourse.html')
    else:
        return render(request, 'augsdapp/ModifyCourse.html')


def DeleteCourse(request):
    if request.method == "GET":
        search_query = request.GET.get('q', None)
        submitbutton = request.GET.get('submit')
        if search_query is not None:
            lookups = Q(courseCode__icontains=search_query) | \
                Q(courseName__icontains=search_query) | \
                Q(courseIC__username__icontains=search_query)
            results = Course.objects.filter(lookups)
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'augsdapp/DeleteCourse.html', context)
        else:
            messages.success(request, 'No Course Found')
            return render(request, 'augsdapp/DeleteCourse.html')
    else:
        return render(request, 'augsdapp/DeleteCourse.html')


def single_course_delete(request, course_pk):
    if request.POST:
        course = get_object_or_404(Course, pk=course_pk)
        course.delete()
    else:
        print("Not a valid request")
    return redirect('DeleteCourse')


def courseDetail(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    sectionList = SecClass.objects.filter(course=course)
    context = {
        "course": course,
        "sectionList": sectionList
    }
    return render(request, 'augsdapp/CourseDetail.html', context)


def updateSection(request, section_pk):
    # clashes and checks not done
    section_selected = get_object_or_404(SecClass, pk=section_pk)
    if request.method == "POST":
        # print(section_selected)
        form = AddSectionForm(request.POST, instance=section_selected)
        if form.is_valid():
                    instructorCheck = SecClass.objects.filter(
                        startTime__gte=form.cleaned_data.get('startTime'),
                        endTime__lte=form.cleaned_data.get('endTime'),
                        days=form.cleaned_data.get('days')).count()
                    classSize = form.cleaned_data.get('classSize')
                    roomSelected = form.cleaned_data.get('room')
                    if instructorCheck != 0:
                        messages.error(
                            request, 'Instructor not available for' +
                            ' the selected time slot')
                        form = AddSectionForm(request.POST)
                    elif classSize > roomSelected.capacity:
                        messages.error(request,
                            'Room cannot accomodate more participants')
                        form = AddSectionForm(request.POST)
                    else:
                        post = form.save(commit=False)
                        post.save()
                        messages.success(request, 'Successful')
                        return redirect('homepage')
        else:
            messages.error(request, 'Invalid Details')
            form = AddSectionForm(instance=section_selected)
    return render(request, 'augsdapp/UpdateSection.html', {
        'section': section_selected,
        'form': form})
