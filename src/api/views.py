from django.http import JsonResponse
from api.serializers import TodoListSerializer
from api.models import TodoList
from rest_framework import viewsets, permissions

class TodoListViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)