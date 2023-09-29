from django.shortcuts import render, redirect
from .models import Student, ClassRoom, StudentProfile

def crud_classroom(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='CRUD/classroom.html', context ={"classrooms" : classrooms,
                                                                          "title" : "Classrooms" })


def classroom_delete(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method =="POST":
        classroom.delete()
        return redirect(crud_classroom)
    return render(request, template_name="CRUD/classroom_delete.html", context={"classroom":classroom})

def classroom_update(request, id):
    classroom=ClassRoom.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        ClassRoom.objects.filter(id=id).update(name= name)
        return redirect('crud_classroom')
    
    return render(request, template_name="CRUD/classroom_update.html", context={"classroom":classroom})

def crud_student(request):
    students= Student.objects.all()
    return render(request, template_name='CRUD/student.html', context={"students":students})

def add_student(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        student=Student.objects.create(name=name, email=email, age=age, classroom_id=1)
        StudentProfile.objects.create(address=address, contact=contact, student=student)
        return redirect("crud_student")
    return render(request, template_name="CRUD/add_student.html", context={"title":"Add Student"})

