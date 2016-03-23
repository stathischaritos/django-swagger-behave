from django.http import JsonResponse
from api.serializers import TodoListSerializer, TodoTaskSerializer, TodoTagSerializer
from api.models import TodoList, TodoTask, TodoTag
from rest_framework import viewsets, permissions

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoTaskViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

class TodoTagViewSet(viewsets.ModelViewSet):
    queryset = TodoTag.objects.all()
    serializer_class = TodoTagSerializer