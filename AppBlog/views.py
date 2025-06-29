from django.shortcuts import render
from .models import Student, Teacher, Article, Paper
from .forms import StudentForm, TeacherForm, ArticleForm, PaperForm
from django.http import HttpResponse

# Index
def index(request):
    return render(request, 'AppBlog/index.html')

#Home
def students_home(request):
    return render(request, 'AppBlog/students_home.html')
def teachers_home(request):
    return render(request, 'AppBlog/teachers_home.html')
def papers_home(request):
    return render(request, 'AppBlog/papers_home.html')
def articles_home(request):
    return render(request, 'AppBlog/articles_home.html')

#Listas
def teachers_list(request):
    return render(request, 'AppBlog/teachers_list.html')

def students_list(request):
    students = Student.objects.all()
    return render(request, 'AppBlog/students_list.html', {'students': students})
def papers_list(request):
    return render(request, 'AppBlog/papers_list.html')
def articles_list(request):
    return render(request, 'AppBlog/articles_list.html')

#Formularios
def students_search(request):
    return render(request, 'AppBlog/students_search.html')
# def students_results(request):
#     return render(request, 'AppBlog/students_results.html')
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
    if request.method == 'POST':
        teachers_form_1 = TeacherForm(request.POST)
        if teachers_form_1.is_valid():
            teacher = Teacher(
                name=teachers_form_1.cleaned_data['name'],
                last_name=teachers_form_1.cleaned_data['last_name'],
                age=teachers_form_1.cleaned_data['age'],
                college=teachers_form_1.cleaned_data['college'],
                email=teachers_form_1.cleaned_data['email'],
                career=teachers_form_1.cleaned_data['career'] 
            )
            teacher.save()
            return render(request, 'AppBlog/teachers_list.html', {'teacher': teacher})
        else:
            return render(request, 'AppBlog/teachers_form.html', {
                'form': teachers_form_1,
                'error_message': 'Hay errores en el formulario.'
            })
    else:
        form = TeacherForm()
        return render(request, 'AppBlog/teachers_form.html', {'form': form})
    
def papers_form(request):
    return render(request, 'AppBlog/papers_form.html')
def articles_form(request):
    return render(request, 'AppBlog/articles_form.html')

#búsquedas


def students_results(request):
    student_name = request.GET.get('name')
    if student_name:
        students = Student.objects.filter(name__icontains=student_name)
        return render(request, "AppBlog/students_results.html", {"name": student_name, "students": students})
    else:
        return render(request, "AppBlog/students_results.html", {"students": []})

    
def teachers_search(request):
    return render(request, 'AppBlog/teachers_search.html')


def papers_search(request):
    return render(request, 'AppBlog/papers_search.html')


def articles_search(request):
    return render(request, 'AppBlog/articles_search.html')

def teachers_results(request):
    return render(request, 'AppBlog/teachers_results.html')
def papers_results(request):
    return render(request, 'AppBlog/papers_results.html')
def articles_results(request):
    return render(request, 'AppBlog/articles_results.html')

