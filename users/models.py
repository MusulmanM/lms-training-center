from django.db import models

# Create your models here.




class User(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'admin'
        TEACHER = 'TEACHER', 'teacher'
        STUDENT = 'STUDENT', 'student'
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='user/')
    gmail = models.CharField(max_length=100, unique=True)
