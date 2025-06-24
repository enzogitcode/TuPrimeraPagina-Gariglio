from django.db import models

# Create your models here.
class User():
    pass
class Student():
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

    #name
    #last_name
    #email
    #subjects
    #college
    pass
class Teacher():
    #name
    #last_name
    #email
    #courses
    pass
class Article():
    #autor
    #tags
    #textPaper
    pass
class Paper():
    #autor
    #tags
    #abstract
    #textPaper
    pass
