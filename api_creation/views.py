from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import student, profile
from .serializers import studentserializer , profileserializer, userserializer
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'User-Register':'/user-register/',
		'User-Login':'/user-login/',
		'List':'/student-list/',
		'Create':'/student-create/',
        'Detail':'student-detail/(?P<pk>\d+)/',
		'Update':'/student-update/(?P<pk>\d+)/',
		'Delete':'/student-delete/(?P<pk>\d+)/',
		}

	return Response(api_urls)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def StudentList(request):
    students = student.objects.all()
    serializer = studentserializer(students, many=True)
        
    return Response(serializer.data)

@api_view(['GET'])
def StudentDetail(request, pk):
	students = student.objects.get(id=pk)
	serializer = studentserializer(students, many=False)

	return Response(serializer.data)

@api_view(['POST'])
def StudentPost(request):
    serializer = studentserializer(data=request.data)
        
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def StudentUpdate(request, pk):
	students = student.objects.get(id=pk)
	serializer = studentserializer(instance=students, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def StudentDelete(request, pk):
    students = student.objects.get(id=pk)
    students.delete()

    return Response('Student Data Deleted')


@api_view(['GET'])
def ProfileList(request):
	pro = profile.objects.all()
	serializer = profileserializer(pro, many=True)

	return Response(serializer.data)

@api_view(['POST'])
def ProfilePost(request):
	serializer = profileserializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UserRegister(request):
	serializer = userserializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	
	return Response(serializer.data)


class UserList(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user = User.objects.all()
		serializer = userserializer(user, many=True)

		return Response(serializer.data)	