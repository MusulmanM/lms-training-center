from rest_framework.serializers import ModelSerializer
from .models import Course, Homework, HomeworkSubmissions, Attandance, Enrollmant


class CourseSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Course



class HomeworkSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Homework



class HomeworkSubmissionsSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = HomeworkSubmissions




class AttandanceSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Attandance




class EnrollmantSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Enrollmant