from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               path('students', views.students_list, name='students_list'),
               path('teachers', views.teachers, name='teachers_list'),
               path('papers', views.papers_list, name='papers_list')
               ]