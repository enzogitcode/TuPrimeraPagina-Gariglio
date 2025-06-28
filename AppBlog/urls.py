from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               
               path('students_home', views.students_home, name='students_home'),
               path('teachers_home', views.teachers_home, name='teachers_home'),
                path('papers_home', views.papers_home, name='papers_home'),
                path('articles_home', views.articles_home, name='articles_home'),

                path('students_search', views.students_search, name='students_search'),
               path('teachers_search', views.teachers_search, name='teachers_search'),
                path('papers_search', views.papers_search, name='papers_search'),
                path('articles_search', views.articles_search, name='articles_search'),

                path('students_results', views.students_results, name='students_results'),
                path('teachers_results', views.teachers_results, name='teachers_results'),
                path('papers_results', views.papers_results, name='papers_results'),
                path('articles_results', views.articles_results, name='articles_results'),

               path('students_list', views.students_list, name='students_list'),
               path('teachers_list', views.teachers_list, name='teachers_list'),
               path('papers_list', views.papers_list, name='papers_list'),
               path('articles_list', views.articles_list, name='articles_list'),

             path('papers_form', views.papers_form, name='papers_form'),
                path('articles_form', views.articles_form, name='articles_form'),
                 path('students_form', views.students_form, name='students_form'),
                 path('teachers_form', views.teachers_form, name='teachers_form'),

               ]