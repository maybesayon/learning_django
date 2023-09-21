from django.urls import path
from .views import student, item, profile
urlpatterns = [
    path("student/", student, name = "student"),
    path("item/", item, name = "item"),
    path("profile/", profile, name = 'profile')
] 