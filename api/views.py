from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from CRUD.models import Student, StudentProfile, ClassRoom
from .serializers import ClassRoomSerializer, ClassRoomModelSerializer, StudentDetailSerializer, StudentModelSerializer
def hello_world(request):
    respose = {
        "message": "Hello World. I'm learning API."
    }

    return JsonResponse(respose)



class HelloWorldView(APIView):
    def get(self, *args, **kwargs):
        response = {
            "message": "Hello World from API view."
        }

        return Response(response)
    
class StudentView(APIView):
    def get (self, *args, **kwargs):
        student =[
            {"name": "Jacob", "age": "40", "address": "TX"},
            {"name": "Jonas", "age": "32", "address": "NY"},
            {"name": "James", "age": "56", "address": "CF"}
            
        ]

        return Response(student)


class StudentFromDBView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs.get("id")
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Invalid Student ID"
            })
        response={
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "classroom": student.classroom.name 
            }
        
        return Response(response)
    
    

class StudentFromDBListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        response=[]
        for student in students:
            data={
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "classroom": student.classroom.name 
            }
            response.append(data)
        return Response(response)
    def post(self, *args, **kwargs):
         #name = request.POST.get("name")
        print(self.request.data)
        name = self.request.data.get("name")
        email = self.request.data.get("email")
        age = self.request.data.get("age")
        classroom = self.request.data.get("classroom")
        Student.objects.create(name=name, email=email, age=age, classroom_id =classroom)
        return Response({
            "detail": "Student added sucessfully"
        })

    
class ProfileFromDBListView(APIView):
    def get(self, *args, **kwargs):
        profile = StudentProfile.objects.all()
        response=[]
        for data in profile:
            data={
               "student": data.student.name,
               "address": data.address,
               "contact": data.contact,
               "pp": data.profile_picture.url
           }
            response.append(data)
        return Response(response)
    

class ClassRoomFromDBView(APIView):
    
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            classroom = ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail":"Invalid Id"
            })
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)
    
class ClassRoomFromDBListView(APIView):
    def get(self, *args, **kwargs):
        classrooms=ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True)
        return Response(serializer.data)
    
    def post(self, *args, **kwargs):
        # serializer = ClassRoomSerializer(data = self.request.data)
        serializer = ClassRoomModelSerializer(data = self.request.data)
        if serializer.is_valid():
            # name = serializer.validated_data.get("name")
            # ClassRoom.objects.create(name=name)
            serializer.save()
            return Response({
                "detail": "Classroom created sucessfully!!"
            })
        
        return Response({
            "detail": "Invalid Request Data !!"
        })

class StudentDetailView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs.get("id")
        students= Student.objects.get(id=id)
        serializer = StudentDetailSerializer(students)
        return Response(serializer.data)
    
class StudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many =True)
        return Response(serializer.data)


    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Student Added Sucessfully!"
            })
        return Response({
            "detail": "Invalid request data"
        })