from rest_framework import serializers
from todo.models import TodoListModel

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListModel
        fields = ('text', 'is_importants', 'is_delete', 'is_complete', 'editMode', 'id')