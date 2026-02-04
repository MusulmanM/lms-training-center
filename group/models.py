from django.db import models
from teacher.models import Teacher
# Create your models here.



class Group(models.Model):
    course = models.ForeignKey("subject.Course", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    max_student = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.course.name
