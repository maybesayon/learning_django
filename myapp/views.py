from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, template_name="myapp/test.html")

def school(request):
    return HttpResponse("I'm learning Python")

def test(request):
    # We can send quarry strings / query parameters in the urls
    # Everything sent after "?" in the url is quarystring
    # Query strings can be multiple and are separated by ampersand(&.)
    name = request.GET.get("name")

    return HttpResponse (f"<h1> My name is {name}</h1>")

def test1(request):
    return render(request, template_name="myapp/test.html")