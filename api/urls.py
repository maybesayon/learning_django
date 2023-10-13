from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import hello_world, HelloWorldView, StudentView, StudentFromDBView,\
StudentFromDBListView, ProfileFromDBListView, ClassRoomFromDBView, ClassRoomFromDBListView, StudentDetailView,\
StudentListView, ProfileListView, ClassRoomAPIView, ClassRoomCreateAPIView, ClassRoomUpdateAPIView, ClassRoomDetailAPIView,\
ClassRoomDeleteAPIView, StudentListAPIView, StudentCreateAPIView, StudentUpdateAPIView, StudentDetailAPIView, StudentDeleteAPIView,\
StudentProfileListAPIView, StudentProfileCreateAPIView, StudentProfileUpdateAPIView, StudentProfileDetailAPIView, StudentProfileDeleteAPIView,\
ClassRoomListCreateAPI, ClassRoomObjectAPIView, ClassRoomViewSet, StudentViewSet, StudentProfileViewSet


router = DefaultRouter()
router.register("classroom-viewset", ClassRoomViewSet)
router.register("student-viewset", StudentViewSet)
router.register("student-profile-viewset", StudentProfileViewSet)

urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("student/",StudentView.as_view()),
    path("student-from-db/<int:id>/", StudentFromDBView.as_view()),
    path("student-from-db/", StudentFromDBListView.as_view()),
    path("classroom-from-db/", ClassRoomFromDBListView.as_view()),
    path("profile-from-db/", ProfileFromDBListView.as_view()),
    path("studentdetailview-from-db/", StudentListView.as_view()),
    path("student-profile-list/", ProfileListView.as_view()),
    path("classroom-from-db/<int:id>/", ClassRoomFromDBView.as_view()),
    path("studentview-from-db/<int:id>/", StudentDetailView.as_view())


]
generic_urls = [
    path("generic-classroom-list/", ClassRoomAPIView.as_view()),
    path("generic-classroom-create/", ClassRoomCreateAPIView.as_view()),
    path("generic-classroom-update/<int:pk>/", ClassRoomUpdateAPIView.as_view()),
    path("generic-classroom-detail/<int:pk>/", ClassRoomDetailAPIView.as_view()),
    path("generic-classroom-delete/<int:pk>/", ClassRoomDeleteAPIView.as_view()),
    path("generic-student-list/", StudentListAPIView.as_view()),
    path("generic-student-create/", StudentCreateAPIView.as_view()),
    path("generic-student-update/<int:pk>/", StudentUpdateAPIView.as_view()),
    path("generic-student-detail/<int:pk>/", StudentDetailAPIView.as_view()),
    path("generic-student-delete/<int:pk>/", StudentDeleteAPIView.as_view()),
    path("generic-studentprofile-list/", StudentProfileListAPIView.as_view()),
    path("generic-studentprofile-create/", StudentProfileCreateAPIView.as_view()),
    path("generic-studentprofile-update/<int:pk>/", StudentProfileUpdateAPIView.as_view()),
    path("generic-studentprofile-detail/<int:pk>/", StudentProfileDetailAPIView.as_view()),
    path("generic-studentprofile-delete/<int:pk>/", StudentProfileDeleteAPIView.as_view()),
    path("generic-classroom/", ClassRoomListCreateAPI.as_view()),
    path("generic-classroom/<int:pk>/", ClassRoomObjectAPIView.as_view()),
    path("login/",obtain_auth_token )
    

]

urlpatterns += generic_urls + router.urls
