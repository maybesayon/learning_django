from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import ListAPIView,\
CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from CRUD.models import Student, StudentProfile, ClassRoom
from .serializers import ClassRoomSerializer, ClassRoomModelSerializer,\
StudentDetailSerializer, StudentModelSerializer, StudentProfileModelSerializer
from .permissions import IsAdminUser
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
            }, status = status.HTTP_400_BAD_Request)
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
        }, status = status.HTTP_201_CREATED)

    
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
            }, status =status.HTTP_400_BAD_REQUEST)
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
            }, status = status.HTTP_201_CREATED)
        
        return Response({
            "detail": "Invalid Request Data !!"
        }, status = 400)

class StudentDetailView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs.get("id")
        students= Student.objects.get(id=id)
        serializer = StudentDetailSerializer(students)
        return Response(serializer.data)
    
class StudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many =True, context={"request" : self.request})
        return Response(serializer.data)


    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Student Added Sucessfully!"
            }, status = status.HTTP_201_CREATED)
        return Response({
            "detail": "Invalid request data"
        }, status = status.HTTP_400_BAD_REQUEST)
    
class ProfileListView(APIView):
    def get(self, *args, **kwargs):
        students = StudentProfile.objects.all()
        serializer=StudentProfileModelSerializer(students, many = True, context={"request": self.request})
        return Response(serializer.data)
    
    def post(self, *args, **kwargs):
        serializer = StudentProfileModelSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail":"Student profile sucessfully"
        }, status = status.HTTP_201_CREATED)

class ClassRoomAPIView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomCreateAPIView(CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomUpdateAPIView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomDetailAPIView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomDeleteAPIView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentDeleteAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentProfileListAPIView(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer

class StudentProfileCreateAPIView(CreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer
    
class StudentProfileUpdateAPIView(UpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer

class StudentProfileDetailAPIView(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer

class StudentProfileDeleteAPIView(DestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer

class ClassRoomListCreateAPI(ListCreateAPIView):
    queryset= ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomObjectAPIView(RetrieveUpdateDestroyAPIView):
    queryset= ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomViewSet(ModelViewSet):
    queryset= ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["name", ]
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminUser(), ]

class StudentViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields =["classroom_id", "classroom__name" ]
    permission_classes =[AllowAny, ]
    queryset= Student.objects.all()
    serializer_class = StudentModelSerializer

    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]

class StudentProfileViewSet(ModelViewSet):
    queryset= StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["student__name","contact" ]
    
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminUser(), ]
    
    