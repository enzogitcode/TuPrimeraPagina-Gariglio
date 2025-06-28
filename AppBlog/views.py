from django.shortcuts import render
from .models import Student, Teacher, Article, Paper
from .forms import StudentForm, TeacherForm, ArticleForm, PaperForm

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
        students_form_1 = StudentForm(request.POST)
        if students_form_1.is_valid():
            student = Student(
                name=students_form_1.cleaned_data['name'],
                last_name=students_form_1.cleaned_data['last_name'],
                age=students_form_1.cleaned_data['age'],
                college=students_form_1.cleaned_data['college'],
                email=students_form_1.cleaned_data['email'],
                career=students_form_1.cleaned_data['career'] 
            )
            student.save()
            return render(request, 'AppBlog/students_list.html', {'student': student})
        else:
            return render(request, 'AppBlog/students_form.html', {
                'form': students_form_1,
                'error_message': 'Hay errores en el formulario.'
            })
    else:
        form = StudentForm()
        return render(request, 'AppBlog/students_form.html', {'form': form})


def teachers_form(request):
    return render(request, 'AppBlog/teachers_form.html')
def papers_form(request):
    return render(request, 'AppBlog/papers_form.html')
def articles_form(request):
    return render(request, 'AppBlog/articles_form.html')