from django.urls import path
from .views import main, features, pricing

urlpatterns = [
    path("features/", features, name = 'features'),
    path ("pricing/", pricing, name = 'pricing'),
    path("", main, name = 'home')
    
]