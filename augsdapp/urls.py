from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('AddCourse/', views.AddCourse, name='AddCourse'),
    path('ModifyCourse/', views.ModifyCourse, name='ModifyCourse'),
    path('DeleteCourse/', views.DeleteCourse, name='DeleteCourse'),
    path('AddSection/<CourseCode>/', views.AddSection, name='AddSection'),
    path('single_course_delete/<course_pk>/',
         views.single_course_delete, name='single_course_delete'),
    path('courseDetail/<course_pk>', views.courseDetail, name='courseDetail'),
    path('updateSection/<section_pk>',
         views.updateSection, name='updateSection')
]
