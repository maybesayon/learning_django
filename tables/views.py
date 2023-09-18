from django.shortcuts import render
from .models import Students, Items


def student(request):
    students= Students.objects.all()
    return render(request, template_name="tables/student.html", context={"students":students})

def item(request):
    items= Items.objects.all()
    return render(request, template_name="tables/item.html", context={"items":items})
