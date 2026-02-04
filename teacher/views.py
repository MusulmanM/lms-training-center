from rest_framework.viewsets import ModelViewSet
from .models import Teacher
from .serializer import TeacherSerializer
# Your views is here

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer