from rest_framework import serializers
from api.models import TodoList, TodoTask, TodoTag
import json

#Serializer for writable nesting inside a TodoTask
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
    tags = TodoTagNestedSerializer(many=True, required=False)

    class Meta:
        model = TodoTask
        fields = ('id', 'title', 'details', 'parentList', 'created', 'tags')

    #Overriding the .create() method to handle creation of tags.
    def create(self, validated_data):
        tags = validated_data.pop('tags')[0]
        task = TodoTask(**validated_data)
        task.save()

        for tag in tags:
            new_tag, created = TodoTag.objects.get_or_create(name=tag)
            new_tag.save()
            new_tag.tasks.add(task)

        return task

    def update(self, task, validated_data):
        tags = validated_data.pop('tags')[0]
        
        #Update Task Info. Looks like a hack but I haven't found an easier way to do this.
        task.__dict__.update(**validated_data)
        task.save()

        #Remove Relation from missing tags.
        for tag in TodoTag.objects.filter(tasks=task):
            if tag.name not in tags:
                tag.tasks.remove(task)
                tag.save()
            else:
                tags.remove(tag.name)

        #Create updated Tags.
        for tag in tags:
            new_tag, created = TodoTag.objects.get_or_create(name=tag)
            new_tag.save()
            new_tag.tasks.add(task)

        return task


class TodoTagSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = TodoTag
        fields = ('id', 'name', 'tasks')

class TodoListSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'description', 'created', 'tasks')
