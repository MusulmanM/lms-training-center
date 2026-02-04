from django.contrib import admin
from .models import Course, Homework, HomeworkSubmissions, Attandance, Enrollmant
# Register your models here.




admin.site.register(Course)
admin.site.register(Homework)
admin.site.register(HomeworkSubmissions)
admin.site.register(Attandance)
admin.site.register(Enrollmant)