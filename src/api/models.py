from __future__ import unicode_literals
from django.db import models

class TodoTag(models.Model):
    name = models.CharField(max_length=30)
    tasks = models.ManyToManyField('TodoTask', related_name="tags")

    def __unicode__(self):
        return self.name

class TodoTask(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    parentList = models.ForeignKey('TodoList', on_delete=models.CASCADE, related_name="tasks")
    
    def __unicode__(self):
        return self.title

class TodoList(models.Model):
    name = models.CharField(max_length=30, unique=True )
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
