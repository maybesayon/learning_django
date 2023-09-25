from django.shortcuts import render

def student_view(request):
    return render(request, template_name='forms/student_view.html')