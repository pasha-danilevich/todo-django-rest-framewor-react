from rest_framework import serializers
from .models import Task

class TaskListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        tasks = [Task(**item) for item in validated_data]
        return Task.objects.bulk_create(tasks)
		

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'
		list_serializer_class = TaskListSerializer


