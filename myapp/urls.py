from django.urls import path
from .views import home
from .views import school
from .views import test
from .views import test1


urlpatterns =[ 
     path("python/", school),
     path("test/", test),
     path("test1/", test1),
     path("", test1)
]

