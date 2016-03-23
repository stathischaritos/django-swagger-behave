from rest_framework import serializers
from api.models import TodoList, TodoTask, TodoTag
import logging
logger = logging.getLogger('todo')

class TodoTagSerializer(serializers.StringRelatedField):
    
    class Meta:
        model = TodoTag
        fields = ('id', 'name')

    def to_internal_value(self, data):
        tags = data.split(",")
        return tags

class TodoTaskSerializer(serializers.ModelSerializer):
    tags = TodoTagSerializer(many=True, required=False)

    class Meta:
        model = TodoTask
        fields = ('id', 'title', 'details', 'parentList', 'created', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags')[0]
        task = TodoTask(**validated_data)
        for tag in tags:
            task.tags.add( TodoTag.objects.create(name=tag) )
        task.save()
        return task

class TodoListSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'description', 'created', 'tasks')
