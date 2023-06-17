from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['t_name', 't_desc', 't_created', 't_updated'] 



