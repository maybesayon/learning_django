from django.urls import path
from .views import hello_world, HelloWorldView, Student
urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("student/",Student.as_view() )
]