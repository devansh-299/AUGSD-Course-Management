from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('AddCourse/', views.AddCourse, name='AddCourse'),
    path('ModifyCourse/', views.ModifyCourse, name='ModifyCourse'),
    path('DeleteCourse/', views.DeleteCourse, name='DeleteCourse'),
    path('AddSection/', views.AddSection, name='AddSection'),
]