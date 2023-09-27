from django.shortcuts import render, redirect
from .models import StudentProfile, Student, ClassRoom

def crud_classroom(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='CRUD/classroom.html', context ={"classrooms" : classrooms,
                                                                          "title" : "Classrooms" })



