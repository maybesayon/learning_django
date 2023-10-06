from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from CRUD.models import ClassRoom, Student
from forms.form  import ClassRoomModelForm


class FirstView(View):
    def get(self, request, *args, **kwargs):
        classrooms= ClassRoom.objects.all()
        form = ClassRoomModelForm()
        return render(request, template_name="classbased/classroom.html",
                      context={"title": "ClassRoom", "classrooms": classrooms, "form": form})

    def post(self, request, *args, **kwargs):   
        form = ClassRoomModelForm(request.POST)
        if form.is_valid():
              form.save()
        return redirect('first_view')
    

class ClassRoomTemplateView(TemplateView):
    template_name = "classbased/classroom.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ClassRoomModelForm()
        classrooms = ClassRoom.objects.all()
        title= ("Classroom")
        context.update(form=form, classrooms=classrooms, title=title)
        return context
    

class ClassRoomView(CreateView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom.html"
    form_class = ClassRoomModelForm
    success_url = reverse_lazy('classbased_classroom')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['classrooms']=ClassRoom.objects.all()
        context["title"] = "Classroom"
        return context
    
class StudentView(ListView):
    queryset = Student.objects.all()
    template_name = 'classbased/student.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    queryset = Student.objects.all()
    template_name = 'classbased/student_detail.html'

    def get_context_data(self, **kwargs):
        print(super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)
    
