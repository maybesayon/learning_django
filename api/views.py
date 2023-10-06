from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
def hello_world(request):
    respose = {
        "message": "Hello World. I'm learning API"
    }

    return JsonResponse(respose)



class HelloWorldView(APIView):
    def get(self, *args, **kwargs):
        response = {
            "message": "Hello World from API view."
        }

        return Response(response)
    
class Student(APIView):
    def get (self, *args, **kwargs):
        student =[
            {"name": "Jacob", "age": "40", "address": "TX"},
            {"name": "Jonas", "age": "32", "address": "NY"},
            {"name": "James", "age": "56", "address": "CF"}
            
        ]

        return Response(student)


