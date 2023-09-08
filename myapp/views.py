from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    content = """
<h1>Hello World</h1>
<h2>I'm learning python</h2>
"""
    return HttpResponse(content)

def school(request):
    return HttpResponse("I'm learning Python")