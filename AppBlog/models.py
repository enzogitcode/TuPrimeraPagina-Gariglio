from django.db import models

# Create your models here.
class User():
    pass
class Student():
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Se creó el estudiante {self.name} {self.last_name} con el correo {self.email}"

class Teacher():
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    email = models.EmailField()
    pass
class Article():
    #autor
    #tags
    keywords = models.CharField(max_length=100, max_size=5)
    date_of_publication = models.DateField(auto_now_add=True)
    #textPaper
    pass
class Paper():
    autor_name = models.CharField(max_length=100)
    autor_email = models.EmailField()
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    textPaper = models.TextField()
    keywords = models.CharField(max_length=100, max_size=5)
    date_of_publication = models.DateField(auto_now_add=True)
    pass
