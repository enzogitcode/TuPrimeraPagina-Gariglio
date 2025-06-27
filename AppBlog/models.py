from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    college = models.CharField(max_length=100)
    courses = models.JSONField(default=list, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f"Se creó el estudiante {self.name} {self.last_name} con el correo {self.email}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    courses = models.JSONField(default=list, blank=True)
    email = models.EmailField()
    def __str__(self):
        return f"Se creó el profesor {self.name} {self.last_name} con el correo {self.email}"
class Article(models.Model):
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    keywords = models.JSONField(default=list, blank=True)
    date_of_publication = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=500)
    textArticle = models.TextField()
    def __str__(self):
        return f"Se creó el artículo {self.title} con el autor {self.author_name} y el correo {self.author_email}"
class Paper(models.Model):
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    textPaper = models.TextField()
    keywords = models.JSONField(default=list, blank=True)
    date_of_publication = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Se creó el artículo {self.title} con el autor {self.autor_name} y el correo {self.autor_email}"
    
    