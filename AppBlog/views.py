from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'AppBlog/index.html')
def teachers(request):
    return render(request, 'AppBlog/teachers_list.html')

def students_list(request):
    return render(request, 'AppBlog/students_list.html')
def papers_list(request):
    return render(request, 'AppBlog/papers_list.html')
def articles(request):
    return render(request, 'AppBlog/articles_list.html')