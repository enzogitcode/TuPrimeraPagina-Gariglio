from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               path('students', views.students_list, name='students_list'),
               path('teachers', views.teachers_list, name='teachers_list'),
               path('papers', views.papers_list, name='papers_list'),
               path('articles', views.articles_list, name='articles_list'),

             path('papers_form', views.papers_form, name='papers_form'),
                path('articles_form', views.articles_form, name='articles_form'),
                 path('students_form', views.students_form, name='students_form'),
                 path('teachers_form', views.teachers_form, name='teachers_form'),

               ]