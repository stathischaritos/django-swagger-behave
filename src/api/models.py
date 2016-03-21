from __future__ import unicode_literals
from django.db import models

class TodoTag(models.Model):
    name = models.CharField(max_length=30)

class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
    tags = models.ManyToManyField(TodoTag)
    created = models.DateTimeField(auto_now_add=True)
    parentList = models.ForeignKey('TodoList', on_delete=models.CASCADE,)

class TodoList(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    tasks = models.ManyToManyField(TodoItem)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='todoLists')

    def __unicode__(self): #__str__
        return self.name

    class Meta:
        app_label = 'api'

