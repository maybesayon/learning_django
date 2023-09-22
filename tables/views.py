from django.shortcuts import render
from .models import Students, Items, StudentProfile, ClassRoom


def student(request):
    students= Students.objects.all()
    return render(request, template_name="tables/student.html", context={"students":students})

def item(request):
    items= Items.objects.all()
    return render(request, template_name="tables/item.html", context={"items":items})

def profile(request):
    profile = StudentProfile.objects.all()
    return render(request, template_name="tables/profile.html", context={"profile":profile})

def classroom(request):
    classroom = ClassRoom.objects.all()
    student= Students.objects.all
    return render(request,template_name="tables/classroom.html", context={"classroom":classroom,
                                                                          "students":student} )    
