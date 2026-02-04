from django.shortcuts import render
from .serializers import GroupSerializer
from .models import Group
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
        UpdateAPIView, DestroyAPIView
# Create your views here.



class GroupViewSet(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class GroupDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
