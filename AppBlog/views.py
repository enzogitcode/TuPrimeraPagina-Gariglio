from django.shortcuts import render
from .models import Student, Teacher, Article, Paper
from .forms import StudentForm, TeacherForm, ArticleForm, PaperForm
from django.http import HttpResponse

# Index
def index(request):
    return render(request, 'AppBlog/index.html')

# students

def students_home(request):
    return render(request, 'AppBlog/students_home.html')
def students_list(request):
    students = Student.objects.all()
    return render(request, 'AppBlog/students_list.html', {'students': students})
def students_search(request):
    return render(request, 'AppBlog/students_search.html')

def students_results(request):
    keyword = request.GET.get('keyword') 
    filtro = request.GET.get('filtro')   

    students = Student.objects.all()

    if keyword and filtro:
        if filtro == 'name':
            students = students.filter(name__icontains=keyword)
        if filtro == 'last_name':
            students = students.filter(last_name__icontains=keyword)
        elif filtro == 'career':
            students = students.filter(career__icontains=keyword)
        elif filtro == 'college':
            students = students.filter(college__icontains=keyword)
        elif filtro == 'email':
            students = students.filter(email__icontains=keyword)
        elif filtro == 'age':
            students = students.filter(age__icontains=keyword)

        context = {
            'students': students,
            'keyword': keyword,
            'filtro': filtro,
        }
        return render(request, "AppBlog/students_results.html", context)
    
    else:
        return render(request, "AppBlog/students_results.html", {
            'students': students,
            'error_message': 'No se encontraron resultados.'
        })

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

# teachers
def teachers_home(request):
    return render(request, 'AppBlog/teachers_home.html')

def teachers_form(request):
    if request.method == 'POST':
        teachers_form_1 = TeacherForm(request.POST)
        if teachers_form_1.is_valid():
            teacher = Teacher(
                name=teachers_form_1.cleaned_data['name'],
                last_name=teachers_form_1.cleaned_data['last_name'],
                age=teachers_form_1.cleaned_data['age'],
                college=teachers_form_1.cleaned_data['college'],
                course=teachers_form_1.cleaned_data['course'],
                email=teachers_form_1.cleaned_data['email'],
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
    

def teachers_results(request):
    keyword = request.GET.get('keyword') 
    filtro = request.GET.get('filtro')   

    teachers = Teacher.objects.all()

    if keyword and filtro:
        if filtro == 'name':
            teachers = teachers.filter(name__icontains=keyword)
        elif filtro == 'last_name':
            teachers = teachers.filter(last_name__icontains=keyword)
        elif filtro == 'course':
            teachers = teachers.filter(course__icontains=keyword)
        elif filtro == 'college':
            teachers = teachers.filter(college__icontains=keyword)
        elif filtro == 'email':
            teachers = teachers.filter(email__icontains=keyword)
        elif filtro == 'age':
            teachers = teachers.filter(age__icontains=keyword)

    context = {
        'teachers': teachers,
        'keyword': keyword,
        'filtro': filtro,
    }
    return render(request, 'AppBlog/teachers_results.html', context)

def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'AppBlog/teachers_list.html', {'teachers': teachers})

def teachers_search(request):
    return render(request, 'AppBlog/teachers_search.html')

# Papers
def papers_home(request):
    return render(request, 'AppBlog/papers_home.html')

def papers_list(request):
    papers = Paper.objects.all()
    return render(request, 'AppBlog/papers_list.html', {'papers': papers})

def papers_form(request):
    return render(request, 'AppBlog/papers_form.html')

from django.shortcuts import render, redirect
from .forms import PaperForm
from .models import Paper

def papers_form(request):
    if request.method == 'POST':
        papers_form_1 = PaperForm(request.POST)
        if papers_form_1.is_valid():
            paper = Paper(
                author_name=papers_form_1.cleaned_data['author_name'],
                author_last_name=papers_form_1.cleaned_data['author_last_name'],
                author_email=papers_form_1.cleaned_data['author_email'],
                subject=papers_form_1.cleaned_data['subject'],
                title=papers_form_1.cleaned_data['title'],
                abstract=papers_form_1.cleaned_data['abstract'],
                text_paper=papers_form_1.cleaned_data['text_paper']  
            )
            paper.save()
            return render(request, 'AppBlog/papers_list.html', {'paper': paper})
        else:
            return render(request, 'AppBlog/papers_form.html', {
                'form': papers_form_1,
                'error_message': 'Hay errores en el formulario.'
            })
    else:
        form = PaperForm()
        return render(request, 'AppBlog/papers_form.html', {'form': form})


def papers_search(request):
    return render(request, 'AppBlog/papers_search.html')

def papers_results(request):
    keyword = request.GET.get('keyword', '').strip()
    filtro = request.GET.get('filtro', '')

    if keyword and filtro in ['author_name', 'author_last_name', 'title', 'subject', 'abstract']:
        filtro_kwargs = {f"{filtro}__icontains": keyword}
        papers = Paper.objects.filter(**filtro_kwargs)
    else:
        papers = Paper.objects.none()

    return render(request, 'AppBlog/papers_results.html', {
        'papers': papers,
        'keyword': keyword,
        'filtro': filtro
    })

# Articles
def articles_home(request):
    return render(request, 'AppBlog/articles_home.html')

def articles_list(request):
    articles= Article.objects.all()
    return render(request, 'AppBlog/articles_list.html', {'articles': articles})
    
def articles_form(request):
    if request.method == 'POST':
        articles_form_1 = ArticleForm(request.POST)
        if articles_form_1.is_valid():
            article = Article(
                author_name=articles_form_1.cleaned_data['author_name'],
                author_last_name=articles_form_1.cleaned_data['author_last_name'],
                author_email=articles_form_1.cleaned_data['author_email'],
                subject=articles_form_1.cleaned_data['subject'],
                title=articles_form_1.cleaned_data['title'],
                resume=articles_form_1.cleaned_data['resume'],
                text_article=articles_form_1.cleaned_data['text_article']
            )
            article.save()
            return render(request, 'AppBlog/articles_list.html', {'article': article})
        else:
            return render(request, 'AppBlog/articles_form.html', {
                'form': articles_form_1,
                'error_message': 'Hay errores en el formulario.'
            })
    else: 
        form= ArticleForm()
        return render(request, 'AppBlog/articles_form.html', {'form': form})

def articles_search(request):
    return render(request, 'AppBlog/articles_search.html')

def articles_results(request):
    keyword = request.GET.get('keyword', '').strip()
    filtro = request.GET.get('filtro', '')

    if keyword and filtro in ['author_name', 'author_last_name', 'title', 'subject', 'resume']:
        filtro_kwargs = {f"{filtro}__icontains": keyword}
        articles = Article.objects.filter(**filtro_kwargs)
    else:
        articles = Article.objects.none()

    return render(request, 'AppBlog/articles_results.html', {
        'articles': articles,
        'keyword': keyword,
        'filtro': filtro
    })


