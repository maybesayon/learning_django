from django.urls import path
from .views import home
from .views import school

urlpatterns =[
     path("world/", home),
     path("python/", school)
]

