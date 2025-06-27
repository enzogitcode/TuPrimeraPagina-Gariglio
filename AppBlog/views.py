from django.shortcuts import render
from .models import student, teacher, paper, article
from forms import StudentForm, TeacherForm, ArticleForm, PaperForm

# Index
def index(request):
    return render(request, 'AppBlog/index.html')

#Listas
def teachers_list(request):
    return render(request, 'AppBlog/teachers_list.html')

def students_list(request):
    return render(request, 'AppBlog/students_list.html')
def papers_list(request):
    return render(request, 'AppBlog/papers_list.html')
def articles_list(request):
    return render(request, 'AppBlog/articles_list.html')

#Formularios
def students_form(request):
    if request.method == 'POST':
        student= student('name')
    
    return render(request, 'AppBlog/students_form.html')
def teachers_form(request):
    return render(request, 'AppBlog/teachers_form.html')
def papers_form(request):
    return render(request, 'AppBlog/papers_form.html')
def articles_form(request):
    return render(request, 'AppBlog/articles_form.html')