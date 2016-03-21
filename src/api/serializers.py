from rest_framework import serializers
from api.models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'description', 'created', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)