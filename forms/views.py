from django.shortcuts import render, redirect
from tables.models import Students, Items

def student_view(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        Students.objects.create(name = name, age = age, address = address, bio = bio, email = email)
        return redirect('student')
    return render(request, template_name='forms/student_view.html')

def item_view(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        price = request.POST.get('price')
        catagory = request.POST.get('catagory')
        uses = request.POST.get('uses')
        description = request.POST.get('description')
        Items.objects.create(name = name, price = price, catagory = catagory, uses = uses, description = description)
        return redirect('item')
    return render(request, template_name='forms/item_view.html')