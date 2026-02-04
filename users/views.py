from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserSerializer
# Your views is here

class TeacherViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer