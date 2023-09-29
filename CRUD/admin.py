from django.contrib import admin

# Register your models here.
from .models import ClassRoom, Student, StudentProfile
admin.site.register(ClassRoom)
admin.site.register(Student)
admin.site.register(StudentProfile)





