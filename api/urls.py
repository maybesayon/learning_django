from django.urls import path
from .views import hello_world, HelloWorldView, StudentView, StudentFromDBView, StudentFromDBListView, ProfileFromDBListView
urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("student/",StudentView.as_view()),
    path("student-from-db/<int:id>/", StudentFromDBView.as_view()),
    path("student-from-db/", StudentFromDBListView.as_view()),
    path("profile-from-db/", ProfileFromDBListView.as_view())
]