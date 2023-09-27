from django.urls import path
from .views import crud_classroom
urlpatterns = [
    path("", crud_classroom, name = "crud_classroom")
]