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

class TaskDetail(APIView):

    def get_object(self, id):
        try:
            task = Task.objects.get(id=id)
           
        except Task.DoesNotExist(): return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return task
    
    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, id):
        task = self.get_object(id)
        serialized = TaskSerializer(task, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


