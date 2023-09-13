from django.urls import path
from .views import home
from .views import school
from .views import test
from .views import test1
from .views import portfolio


urlpatterns =[ 
     path("python/", school),
     path("test/", test),
     path("yay/", test),
     path("portfolio/", portfolio),
     path("", test1)
]

