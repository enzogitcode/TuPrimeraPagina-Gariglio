from django import forms

class StudentForm(forms.Forms):
    name = forms.CharField(max_length=100, label='Nombre')
    last_name = forms.CharField(max_length=100, label='Apellido')
    age = forms.IntegerField(label='Edad', min_value=0, max_value=120)
    college = forms.CharField(max_length=100, label='Colegio')
    email = forms.EmailField(label='Correo Electrónico')

class TeacherForm(forms.Forms):
    name = forms.CharField(max_length=100, label='Nombre')
    last_name = forms.CharField(max_length=100, label='Apellido')
    age = forms.IntegerField(label='Edad', min_value=0, max_value=120)
    courses = forms.CharField(max_length=100, label='Cursos')
    email = forms.EmailField(label='Correo Electrónico')

class ArticleForm(forms.Forms):
    author_name = forms.CharField(max_length=100, label='Nombre del Autor')
    author_last_name = forms.CharField(max_length=100, label='Apellido del Autor')
    author_email = forms.EmailField(label='Correo Electrónico del Autor')
    keywords = forms.CharField(max_length=500, label='Palabras Clave', required=False)
    title = forms.CharField(max_length=200, label='Título')
    resume = forms.CharField(max_length=500, label='Resumen')
    textArticle = forms.CharField(widget=forms.Textarea, label='Texto del Artículo')

class PaperForm(forms.Forms):
    author_name = forms.CharField(max_length=100, label='Nombre del Autor')
    author_last_name = forms.CharField(max_length=100, label='Apellido del Autor')
    author_email = forms.EmailField(label='Correo Electrónico del Autor')
    title = forms.CharField(max_length=200, label='Título')
    abstract = forms.CharField(max_length=500, label='Resumen')
    textPaper = forms.CharField(widget=forms.Textarea, label='Texto del Artículo')
    keywords = forms.CharField(max_length=500, label='Palabras Clave', required=False)
