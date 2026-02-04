from .models import Course, Homework, HomeworkSubmissions, Attandance, Enrollmant
from .serializer import CourseSerializer, HomeworkSerializer, HomeworkSubmissionsSerializer, AttandanceSerializer, EnrollmantSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
        UpdateAPIView, DestroyAPIView

# Create your views here.

# cours

class CourseApiVIew(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()




# Homework



class HomeworkApiVIew(ListCreateAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()


class HomeworkDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()




# homework S



class HomeworkSubmissionsApiVIew(ListCreateAPIView):
    serializer_class = HomeworkSubmissionsSerializer
    queryset = HomeworkSubmissions.objects.all()


class HomeworkSubmissionsDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSubmissionsSerializer
    queryset = HomeworkSubmissions.objects.all()




# Attandance



class AttandanceApiVIew(ListCreateAPIView):
    serializer_class = AttandanceSerializer
    queryset = Attandance.objects.all()


class AttandanceDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = AttandanceSerializer
    queryset = Attandance.objects.all()





# Enrollmant



class EnrollmantApiVIew(ListCreateAPIView):
    serializer_class = EnrollmantSerializer
    queryset = Enrollmant.objects.all()


class EnrollmantDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = EnrollmantSerializer
    queryset = Enrollmant.objects.all()



