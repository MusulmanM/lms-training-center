from django.urls import path
from .views import CourseApiVIew, CourseDetailApiVIew
from .views import HomeworkApiVIew, HomeworkDetailApiVIew
from .views import HomeworkSubmissionsApiVIew, HomeworkSubmissionsDetailApiVIew
from .views import AttandanceApiVIew, AttandanceDetailApiVIew
from .views import EnrollmantApiVIew, EnrollmantDetailApiVIew


urlpatterns = [
    path("course/", CourseApiVIew.as_view()),
    path("course/<int:pk>/", CourseApiVIew.as_view()),

    path("course/", CourseDetailApiVIew.as_view()),
    path("course/<int:pk>/", CourseDetailApiVIew.as_view()),



    
    path("homework/", HomeworkApiVIew.as_view()),
    path("homework/<int:pk>/", HomeworkApiVIew.as_view()),

    path("homework/", HomeworkDetailApiVIew.as_view()),
    path("homework/<int:pk>/", HomeworkDetailApiVIew.as_view()),




    path("homeworks/", HomeworkSubmissionsApiVIew.as_view()),
    path("homeworks/<int:pk>/", HomeworkSubmissionsApiVIew.as_view()),

    path("homeworks/", HomeworkSubmissionsDetailApiVIew.as_view()),
    path("homeworks/<int:pk>/", HomeworkSubmissionsDetailApiVIew.as_view()),




    path("attandance/", AttandanceApiVIew.as_view()),
    path("attandance/<int:pk>/", AttandanceApiVIew.as_view()),

    path("attandance/", AttandanceDetailApiVIew.as_view()),
    path("attandance/<int:pk>/", AttandanceDetailApiVIew.as_view()),




    path("enrollmant/", EnrollmantApiVIew.as_view()),
    path("enrollmant/<int:pk>/", EnrollmantApiVIew.as_view()),

    path("enrollmant/", EnrollmantDetailApiVIew.as_view()),
    path("enrollmant/<int:pk>/", EnrollmantDetailApiVIew.as_view()),
    ]