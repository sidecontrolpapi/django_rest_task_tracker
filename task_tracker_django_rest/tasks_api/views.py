from rest_framework import serializers
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.views import status

# Create your views here.
class TasksApi(APIView):

    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)