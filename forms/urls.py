from django.urls import path
from .views import student_view, item_view

urlpatterns = [
    path('items', item_view, name = "item_view"),
    path('', student_view, name = "student_view")
]
