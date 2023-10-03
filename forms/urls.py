from django.urls import path
from .views import student_view, item_view, classroom, model_classroom

urlpatterns = [
    path('items', item_view, name = "item_view"),
    path("classroom/", classroom, name="forms_classroom"),
    path("model-classroom/", model_classroom, name = "model_clasroom"),
    path('', student_view, name = "student_view")
]
