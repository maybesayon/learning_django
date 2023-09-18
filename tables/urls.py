from django.urls import path
from .views import student, item

urlpatterns = [
    path("student/", student, name = "student"),
    path("item/", item, name = "item")
] 