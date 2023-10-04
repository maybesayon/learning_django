from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from CRUD.models import ClassRoom
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