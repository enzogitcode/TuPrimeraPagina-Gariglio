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
    keywords = models.CharField(max_length=100)
    date_of_publication = models.DateField(auto_now_add=True)
    #textPaper
    pass
class Paper():
    #autor
    #tags
    #abstract
    #textPaper
    # date_of_publication = models.DateField(auto_now_add=True)
    pass
