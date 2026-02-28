from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
        UpdateAPIView, DestroyAPIView
from .models import User
from .serializer import UserSerializer
# Your views is here

class UserViewSet(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer