from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'AppBlog/index.html')
def teachers_list(request):
    return render(request, 'AppBlog/teachers_list.html')

def students_list(request):
    return render(request, 'AppBlog/students_list.html')
def papers_list(request):
    return render(request, 'AppBlog/papers_list.html')
def articles_list(request):
    return render(request, 'AppBlog/articles_list.html')


def papers_form(request):
    return render(request, 'AppBlog/papers_form.html')
def articles_form(request):
    return render(request, 'AppBlog/articles_form.html')
def students_form(request):
    return render(request, 'AppBlog/students_form.html')
def teachers_form(request):
    return render(request, 'AppBlog/teachers_form.html')