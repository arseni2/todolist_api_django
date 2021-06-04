from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import TodoListModel
from todo.serializers import TodoListSerializer

class CreateTodo(generics.ListCreateAPIView):
    queryset = TodoListModel.objects.all()
    serializer_class = TodoListSerializer

class ImportantTodo(generics.ListAPIView):
    queryset = TodoListModel.objects.filter(is_importants=True)
    serializer_class = TodoListSerializer

class EditTodo(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = TodoListModel.objects.all()
    serializer_class = TodoListSerializer
@api_view(['POST', ])
def addToImportantOrBin(request):
    todo_id = request.POST.get('todo_id')
    current_todo = TodoListModel.objects.get(id=todo_id)
    if request.POST.get('is_delete'):
        current_todo.is_delete = True
    else:
        current_todo.is_importants = True
    current_todo.save()
    s = TodoListSerializer(current_todo).data
    return Response(s)
@api_view(['POST', ])
def toComplete(request):
    todo_id = request.POST.get('todo_id')
    current_todo = TodoListModel.objects.get(id=todo_id)
    current_todo.is_complete = True
    current_todo.save()
    s = TodoListSerializer(current_todo).data
    return Response(s)

@api_view(['GET', ])
def todoBin(request):
    todo = TodoListModel.objects.filter(is_delete=True)
    s = TodoListSerializer(todo, many=True).data
    return Response(s)

