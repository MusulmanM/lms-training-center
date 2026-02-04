from django.db import models
from users.models import User
# Create your models here.





class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=155, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)




    def __str__(self):
        return self.user