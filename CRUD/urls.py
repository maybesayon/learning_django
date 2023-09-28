from django.urls import path
from .views import crud_classroom, classroom_delete, classroom_update
urlpatterns = [
    path("classroom/delete/<int:id>/", classroom_delete, name = "classroom_delete"),
    path("classroom/update/<int:id>/", classroom_update, name="classroom_update"),
    path("", crud_classroom, name = "crud_classroom")
]