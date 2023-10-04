from django.urls import path
from .views import FirstView, ClassRoomTemplateView

urlpatterns=[
    path("class-temp/", ClassRoomTemplateView.as_view(), name="class_temp"),
    path("",FirstView.as_view(), name="first_view"),
]