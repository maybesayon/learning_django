from rest_framework import serializers
from CRUD.models import ClassRoom, Student, StudentProfile

class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id","name"]

class StudentDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    classroom = serializers.IntegerField()

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "classroom"]


    def get_fields(self):
        fields = super().get_fields()
        request= self.context.get("request")
        if request and request.method.lower() == 'get':
            fields['classroom']=ClassRoomModelSerializer()
        return fields
    

class StudentProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["student", "profile_picture", "address", "contact"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method.lower()== 'get':
            fields['student']= StudentModelSerializer()
        return fields



   

    

