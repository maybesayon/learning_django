from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, template_name="myapp/test.html")

def school(request):
    return HttpResponse("I'm learning Python")

def test(request):
    return render(request, template_name="myapp/test1.html")

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

def portfolio(request):
    return render(request, template_name="myapp/index.html")