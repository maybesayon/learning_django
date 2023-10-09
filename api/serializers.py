from rest_framework import serializers
from CRUD.models import ClassRoom, Student

class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["name"]

class StudentDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    classroom = serializers.IntegerField()

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "classroom"]