from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('O título da tarefa é obrigatório.')
        return value.strip()
    
    def validate_description(self, value):
        if value:
            return value.strip()
        return value