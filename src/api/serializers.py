from rest_framework import serializers
from api.models import TodoList, TodoTask, TodoTag
import json

class TodoTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TodoTag
        fields = ('id', 'name')


class TodoTagNestedSerializer(serializers.RelatedField):
    queryset = TodoTag.objects.all()
    
    def to_internal_value(self, data):
        return data.split(",")

    def to_representation(self, data):
        return data.name

    class Meta:
        model = TodoTag
        fields = ('id','name')

class TodoTaskSerializer(serializers.ModelSerializer):
    tags = TodoTagNestedSerializer(many=True)

    class Meta:
        model = TodoTask
        fields = ('id', 'title', 'details', 'parentList', 'created', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags')[0]
        task = TodoTask(**validated_data)
        task.save()

        for tag in tags:
            new_tag, created = TodoTag.objects.get_or_create(name=tag)
            new_tag.save()
            new_tag.tasks.add(task)

        return task

class TodoListSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'description', 'created', 'tasks')
