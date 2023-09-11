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
    peoples_info= [
        {"First": "Jon", "Last": "Harris", "Address": "KTM"},
        {"First": "Walter", "Last": "White", "Address": "NY"},
        {"First": "Aflie", "Last": "Soloman", "Address": "TEX"},
        {"First": "Gustavo", "Last": "Fring", "Address": "PKR"}
    ]
    table_heading = "People Information"
    return render(request, template_name="myapp/test.html",
                   context={"heading": table_heading, "infos": peoples_info})