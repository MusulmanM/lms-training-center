from django.db import models
from teacher.models import Teacher
from group.models import Group
from student.models import Student
# Create your models here.



class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    davomiyligi = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return self.name
    




class Homework(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    homework = models.TextField(blank=True, null=True)
    content = models.FileField(upload_to='homework/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group
    





class HomeworkSubmissions(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    content = models.FileField(upload_to='student-homework/', blank=True, null=True)
    content_text = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)
    teacher_commit = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.user.username
    




class Attandance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey("group.Group", on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    attandance_date = models.DateField()

    def __str__(self):
        return self.student.user.username







class Status(models.TextChoices):
    ACTIVE = 'active', "Faol"
    FINISHED = 'finished', 'Tugallagan'
    DROPPED = 'dropped', 'Chetlashtirilgan'

class Enrollmant(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateField()
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ACTIVE)

    def __str__(self):
        return self.student.user.username





