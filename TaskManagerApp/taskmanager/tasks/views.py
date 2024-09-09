from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def task_statistics(request):
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='completed').count()
    return Response({
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    })
